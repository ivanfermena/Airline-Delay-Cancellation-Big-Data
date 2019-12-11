---
layout: post
title:  "Análisis de los retrasos entre cada Origen-Destino y, si éste se produce en el tiempo de vuelo"
description: Estudiamos si el retraso entre un origen y un destino se produce en el tiempo de vuelo, comparando el tiempo que se esperaba de vuelo con el usado realmente. 
categories: batch
---

![sample post]({{site.baseurl}}/images/plane-red.png)

## Descripción:

En este apartado se va a realizar un análisis de los retrasos con la finalidad de averiguar si este problema es debido al excesivo tiempo del avion en el aire. Conocemos los diferentes tiempos de un vuelo, desde el tiempo en pista hasta las horas en las que levanta las ruedas de la pista y las coloca sobre ésta de nuevo, en el aterrizaje. Con todos estos datos se puede hacer un análisis meticuloso de dicho caso de uso.

## Ficheros 

* `delay_per_journey.py`
* `2009-2018.csv`

## Ejecución

>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    delay_per_journey.py

>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /delay_per_journey/*.csv

## Código

A continuación mostraremos las secciones más significativas del código y su salida. De este modo se comprende el procedimiento usado para las tranformaciones del código y análisis. Lo primero que vemos es la importación de todas las librerías necesarias para el uso correcto del ejemplo. Hemos optado por el uso de Pandas, por orientación matemática y de tratamiento de dataframes que ofrece, además de la integración tan buena que tiene con Apache Spark. También se importa el contexto de Spark, necesario para trabajar en Apache Spark y hemos creado un contexto de spark SQL para poder lanzar consultas sobre el dataframe.

{% highlight python %}

from pyspark import SparkContext
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as fn
from pyspark.sql.functions import col
import pandas as pd

sc = SparkContext()
spark = SparkSession.builder.appName("Aircraft-Delay-Cancelation").getOrCreate()

{% endhighlight %}

Omitiendo la limpieza de datos previa (eliminar NA, vacios...), ahora realizamos una primera valoración del caso de uso, viendo los retrasos producidos agrupándolos por origen y destino. De este modo tenemos en cómputo global cuáles han sido aquellos vuelos con más retrasos en total de todos los datasets.
Nos ha parecido interesante ordenarlos en ambos sentidos, es decir, también conocer cuáles son los destinos que menos retrasos tenían. 

{% highlight python %}

df_airports = spark.createDataFrame(df_cleaned[['ORIGIN', 'DEST', 'DEP_DELAY']])

# Comprobamos los tipos de las columnas para no tener error de typos en el sum
print(df_airports.dtypes)

# Cogemos las columnas que nos interesan y las casteamos a Integer
df_airports = df_airports.withColumn('DEP_DELAY', col("DEP_DELAY").cast(IntegerType()))

# Agrupamos por Origen y destino
df_gb_airports = df_airports.groupby(['ORIGIN', 'DEST'])

# Hacemos la suma por del retraso a partir del grupo
df_grouped = df_gb_airports.agg(fn.sum(col('DEP_DELAY')).alias('DEP_DELAY_SUM'))

df_grouped_desc = df_grouped.sort(fn.desc("DEP_DELAY_SUM"))
df_grouped_asce = df_grouped.sort(fn.asc("DEP_DELAY_SUM"))

# Comparativa por ambos lados, tanto los que tienen menos como los que mas.
print(df_grouped_asce.show())
print(df_grouped_desc.show())

{% endhighlight %}

Un vez realizado este análisis previo, obtenemos el tiempo en el aire que ha estado el vuelo. eliminando el tiempo de despegue y aterrizaje, para finalmente, restarlo al tiempo esperado de vuelo. De este modo podemos saber si el tiempo de vuelo ha sido un factor principal para el retraso producido, todo esto agrupado por origen y destino. 

{% highlight python %}

# CRS_ELAPSED_TIME = Tiempo planeado del vuelo
# ACTUAL_ELAPSED_TIME = AIR_TIME + TAXI_IN + TAXI_OUT
df_airports_with_fly_time = spark.createDataFrame(df_cleaned[['ORIGIN', 'DEST', 'CRS_ELAPSED_TIME', 'ACTUAL_ELAPSED_TIME', 'TAXI_IN', 'TAXI_OUT']])

df_airports_with_fly_time = df_airports_with_fly_time.withColumn('TIME_FLY', 
    df_airports_with_fly_time['ACTUAL_ELAPSED_TIME'] - (df_airports_with_fly_time['TAXI_IN'] + df_airports_with_fly_time['TAXI_OUT']))

df_airports_with_fly_time = df_airports_with_fly_time.withColumn('DIF_TIME_FLY',
    df_airports_with_fly_time['CRS_ELAPSED_TIME'] - df_airports_with_fly_time['TIME_FLY'])

df_group_with_fly_time = df_airports_with_fly_time.groupby(['ORIGIN', 'DEST'])

df_fly_time_agruped = df_group_with_fly_time.agg(fn.sum(col('CRS_ELAPSED_TIME')).alias('ELAPSED_TIME'), 
                                                fn.sum(col('TIME_FLY')).alias('TIME_FLY'),
                                                fn.sum(col('DIF_TIME_FLY')).alias('DIF_TIME_FLY'))

df_fly_time_agruped_desc = df_fly_time_agruped.sort(fn.asc("DIF_TIME_FLY"))

{% endhighlight %}

## Resultado

Los resultados obtenidos se muestran a continuación, primero ordenados por aquellos de menor retraso en el vuelo y después de mayor a menor. Con estos datos somos capaces de saber cuáles son los vuelos que tienen más retrasos en el vuelo y tomar medidas para solucionarlo. Sería una buena base para proceder a estudiar el motivo del retraso de esos vuelos que se encuentran peor parados en los los tiempos de vuelo.

Ordenados de menor a mayor: 

    +------+----+------------+--------+------------+ 
    |ORIGIN|DEST|ELAPSED_TIME|TIME_FLY|DIF_TIME_FLY| 
    +------+----+------------+--------+------------+ 
    |   SWF| PGD|       175.0|   196.0|       -21.0|
    |   PDX| LIH|       325.0|   337.0|       -12.0|
    |   CMH| DFW|       176.0|   187.0|       -11.0|
    |   ORD| RAP|       150.0|   157.0|        -7.0|
    |   HPN| RSW|       199.0|   204.0|        -5.0|
    |   JNU| PSG|        45.0|    48.0|        -3.0|
    |   RAP| ORD|       141.0|   142.0|        -1.0|
    |   PVD| PIE|       195.0|   194.0|         1.0|
    |   BOI| SAN|       286.0|   284.0|         2.0|
    |   PIT| DFW|       165.0|   163.0|         2.0|
    |   AZA| BOI|       120.0|   117.0|         3.0|
    |   CHS| MIA|        99.0|    96.0|         3.0|
    |   PDX| DTW|       243.0|   239.0|         4.0|
    |   ALB| TPA|       190.0|   186.0|         4.0|
    |   GSP| FLL|       109.0|   105.0|         4.0|
    |   AUS| MSY|        75.0|    69.0|         6.0|
    |   ACY| PBI|       156.0|   149.0|         7.0|
    |   HGR| SFB|       134.0|   127.0|         7.0|
    |   HNL| SJC|       300.0|   293.0|         7.0|
    |   OGG| SJC|       585.0|   578.0|         7.0|
    +------+----+------------+--------+------------+

Ordenados de mayor a menor: 

    +------+----+------------+--------+------------+
    |ORIGIN|DEST|ELAPSED_TIME|TIME_FLY|DIF_TIME_FLY|
    +------+----+------------+--------+------------+
    |   LAX| SFO|      2449.0|  1439.0|      1010.0|
    |   SFO| SEA|      3177.0|  2269.0|       908.0|
    |   SFO| LAX|      2161.0|  1282.0|       879.0|
    |   SEA| SFO|      3248.0|  2371.0|       877.0|
    |   DEN| LAX|      3202.0|  2410.0|       792.0|
    |   ORD| LAX|      4726.0|  3963.0|       763.0|
    |   EWR| SFO|      5864.0|  5103.0|       761.0|
    |   MCO| EWR|      3027.0|  2266.0|       761.0|
    |   LAX| SEA|      2814.0|  2110.0|       704.0|
    |   EWR| LAX|      5296.0|  4606.0|       690.0|
    |   LGA| ORD|      2273.0|  1589.0|       684.0|
    |   FLL| EWR|      3022.0|  2341.0|       681.0|
    |   DEN| SFO|      3237.0|  2567.0|       670.0|
    |   JFK| LAX|      5413.0|  4774.0|       639.0|
    |   BOS| SFO|      4476.0|  3872.0|       604.0|
    |   SFO| EWR|      5170.0|  4568.0|       602.0|
    |   DEN| LAS|      2270.0|  1692.0|       578.0|
    |   ORD| SFO|      3719.0|  3154.0|       565.0|
    |   SEA| LAX|      2503.0|  1942.0|       561.0|
    |   LAX| HNL|      3742.0|  3183.0|       559.0|
    +------+----+------------+--------+------------+
