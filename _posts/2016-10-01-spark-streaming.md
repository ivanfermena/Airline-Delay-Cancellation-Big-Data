---
layout: post
title:  "Actualización en tiempo real de los vuelos con más retrasos por día"
description: A continuación mostraremos el caso de uso elegido para realizar la parte de procesamiento en streming con Spark Streaming. En ésta, hemos elegido mostrar los vuelos con más retrasos (top 10) entre dos ciudades de EEUU, usando como ventana, 3 segundo y reiniciando una vez al día dicha clasificación.
categories: streaming
---

![sample post]({{site.baseurl}}/images/spark-streaming.png)

## Descripción: Muchos datos en batch pero sin datos en tiempo real

La principal problemática que hemos encontrado a la hora de analizar en tiempo real los datos, es justamente, la falta de una fuente de datos en tiempo real. Sabemos que en el caso de uso que hemos elegido se analizan muchos datos en tiempo real y por eso es necesario realizar este apartado.

Para ello hemos extraído una parte de los datos y hemos creado un socket que envía datos cada cierto tiempo por dicho canal, de este modo somos capaces de obtener por Spark Streaming los datos y analizar todo lo necesario. El socket lee un "csv" dado por nosotros y envía por esa comunicación una línea cada vez. En nuestro caso, ya que teníamos el socket abierto nos ha parecido interesante devolver los datos analizados al cliente (proveedor de líneas) para completar la comunicación.  

## Ficheros 

* `clientSparkStreaming.py`
* `serverSparkStreaming.py`

## Ejecución

Para ejecutar este ejemplo es necesario ejecutar primero el server y esperar a que se quede en espera un par de segundos.

{% highlight python %}
spark-submit serverSparkStreaming.py
{% endhighlight %}

Tras la espera de esos segundos y cuando el terminal no muestra más mensajes, se puede lanzar el cliente:

{% highlight python %}
spark-submit clientSparkStreaming.py
{% endhighlight %}

## Código

A continuación mostraremos los dos archivos de python que hemos usado para el procesamiento en streaming. Comenzaremos con el Cliente, ya que es el más sencillo y no tiene secciones de código de Spark, ya que no realiza ningún procesamiento ni transformación. En el caso del Cliente sólo es necesario importar la librería de "sockets" y "time".

### Cliente

**Code:** El código del socket del cliente se muestra entero ya que es claro y sencillo. Abriendo una conexion específica en local y enviando con ".send" cada una de las líneas leídas cada 3 segundos.

{% highlight python %}

import socket
import time
 
def Main():
        host = 'localhost'
        port = 9999
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        while 1:
            with open("./../src/data/streaming/*.csv") as fp:
                line = fp.readline()
                while line:
                    time.sleep(3)
                    line = fp.readline()

                    mySocket.send(line.strip().encode())

                    data = mySocket.recv(1024).decode()
                    print (" - " + data)
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()

{% endhighlight %}

### Server

Se analizará ahora por secciones, el código de spark usado para analizar dichas líneas enviadas desde el cliente. Primero empezaremos importando todas las librerías necesarias de pyspark, con las que analizaremos cada una de las líneas y realizaremos consultas sobre el dataframe. Como en el cliente, necesitaremos el socket y Pandas para el análisis de los dataframes. Se ha usado Pandas debido a la facilidad a la hora de realizar operaciones sobre conjuntos y su buena integración con Apache Spark. Por último, se ha importado "io" de "StringIO" para poder tratar un texto específico (una línea del csv) como si fuera una entrada de un fichero leído.

{% highlight python %}

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as fn
from pyspark.sql.functions import col
import socket
from io import StringIO

import pandas as pd

names_col = ["FL_DATE","OP_CARRIER","OP_CARRIER_FL_NUM","ORIGIN","DEST","CRS_DEP_TIME","DEP_TIME","DEP_DELAY", \
"TAXI_OUT","WHEELS_OFF","WHEELS_ON","TAXI_IN","CRS_ARR_TIME","ARR_TIME","ARR_DELAY","CANCELLED","CANCELLATION_CODE", \
"DIVERTED","CRS_ELAPSED_TIME","ACTUAL_ELAPSED_TIME","AIR_TIME","DISTANCE","CARRIER_DELAY","WEATHER_DELAY","NAS_DELAY", \
"SECURITY_DELAY","LATE_AIRCRAFT_DELAY", "Unnamed"]

{% endhighlight %}

A continuación tenemos la función que realiza el procesamiento de cada una de la líneas, y actualiza el dataframe que contiene el top 10 de vuelos que tienen más retraso. Se explicará, con comentarios en el código, cada una de las líneas, pero en conjunto se lee la línea extraída de argumento, comprueba si es el mismo día de procesamiento y si no vacía el dataframe acumulador, tras esto, realiza las agrupaciones determinadas por ORIGEN, DESTINO y DEP_DELAY. Finalmente se ordenan por ese "DEP_DELAY" y devuelve dicho dataframe. 

{% highlight python %}

def proccessSpark(sc, ssc, spark, line, df_top, today_date):


    df_line = pd.read_csv(StringIO(line), names=names_col)

    # Obtener el top 10 de delays por dia

    if today_date != df_line["FL_DATE"].item():
        today_date = df_line["FL_DATE"].item()
        df_top = pd.DataFrame(columns=names_col)

    df_top = df_top.append(df_line)

    df_airports = spark.createDataFrame(df_top[['ORIGIN', 'DEST', 'DEP_DELAY']])

    # Cogemos las columnas que nos interesan y las casteamos a Integer
    df_airports = df_airports.withColumn('DEP_DELAY', col("DEP_DELAY").cast(IntegerType()))

    # Agrupamos por Origen y destino
    df_gb_airports = df_airports.groupby(['ORIGIN', 'DEST'])

    # Hacemos la suma por del retraso a partir del grupo
    df_grouped = df_gb_airports.agg(fn.sum(col('DEP_DELAY')).alias('DEP_DELAY_SUM'))

    df_top_ten = df_grouped.sort(fn.desc("DEP_DELAY_SUM"))

    print(df_top_ten.show(10))

    # Actualizar ese top 10 en tiempo real

    return df_top, today_date

{% endhighlight %}

El siguiente código sólo genera la estructura necesaria para que se pueda realizar el procesamiento correctamente, especificado más arriba. Entre ellos se inicia el dataframe que se va a usar a lo largo de la aplicación y el socket necesario para obtener los datos del cliente.

{% highlight python %}

def Main():
    host = "localhost"
    port = 9999

    today_date = "1995-01-01"
    data_top = pd.DataFrame(columns=names_col)
    
    mySocket = socket.socket()
    mySocket.bind((host,port))

    # Create a local StreamingContext with two working thread and batch interval of 1 second
    sc = SparkContext("local[2]", "NetworkSpark")
    ssc = StreamingContext(sc, 3)

    spark = SparkSession.builder.appName("Aircraft-Delay-Streaming").getOrCreate()
     
    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))

    while True:
        line = conn.recv(1024).decode()

        if not line:
            break
            
        data_top, today_date = proccessSpark(sc, ssc, spark, line, data_top, today_date)

        conn.send(data_top.to_string().encode())
             
    conn.close()
     
if __name__ == '__main__':
    Main()

{% endhighlight %}

## Resultados 

En esta sección mostramos los resultados del procesamiento en streaming. En el primero se ve sólo al producirse dos iteraciones del socket y en la segunda tras haberse producido un número elevado de iteraciones. Aquí se puede ver, cómo van evolucionando los 10 vuelos que tienen más retraso, de este modo, se puede intentar enviar alertas a los vuelos para adaptar los tiempos y reducir lo máximo estos tiempos o que por lo menos no aumenten.

Output en segunda iteración:

    +------+----+-------------+
    |ORIGIN|DEST|DEP_DELAY_SUM|
    +------+----+-------------+
    |   EWR| DEN|           -5|
    |   LAS| SFO|           -8|
    +------+----+-------------+

Output en "n" iteraciones:

    +------+----+-------------+
    |ORIGIN|DEST|DEP_DELAY_SUM|
    +------+----+-------------+
    |   LAX| SAN|          299|
    |   EWR| BTV|          134|
    |   IND| ORD|           94|
    |   MSY| EWR|           48|
    |   ORD| MCI|           41|
    |   ORD| CLT|           26|
    |   ALB| ORD|           18|
    |   IAD| DEN|           18|
    |   ORD| DTW|           17|
    |   IAD| FLL|           16|
    +------+----+-------------+
    
only showing top 10 rows
