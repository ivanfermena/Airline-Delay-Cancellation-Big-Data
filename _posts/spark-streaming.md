---
layout: post
title:  "Actualizacion en tiempo real de los vuelos con mas retrasos por dia"
description: A continuacion mostraremos el caso de uso elegido para realizar la parte de procesamiento en streming con Spark Streming. En esta hemos elegido mostrar los vuelos con mas retrasos (top 10) entre dos ciudades de EEUU, usando como ventana 3 segundo y reiniciando una vez al dia dicha clasificacion.
categories: Streming
---

![sample post]({{site.baseurl}}/images/image-2.png)


## Muchos datos en batch pero sin datos en tiempo real

La principal problematica que hemos encontrado a la hora de analizar en tiemp real los datos, es justamente la falta de una fuente de datos en tiempo real. Sabemos que en el caso de uso que hemos elegido se analizan muchos datos en tiempo real y por eso es necesario realizar este apartado.

Para ello hemos extraido una parte de los datos y hemos creado un socket que envia datos cada cierto tiempo por dicha comunicación, de este modo somos capaces de obtener por Spark Streaming los datos y analizarlos tood lo necesario. El socket lee un "csv" dado por nosotros y envia por esa comunicación una linea cada vez. En nuestro caso, ya que teniamos el socket abierto nos ha parecido interesante devolver los datos analizados al cliente (proveedor de lineas) para completar la comunicación.  

## Código

A continucacion mostraremos los dos archivos de pyhon que hemos usado para el procesamiento en streaming. Comenzaremos con el Cliente, ya que es el mas sencillo y no tiene secciones de codigo de Spark, ya que no realiza ningun porcesamiento ni ransformación.

### Cliente

**Code:** Let's keep it to its length and let it not take the whole width.
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

Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit.

This is a simple markdown table

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |



Use below code to show **Table of Contents** on a page

{% highlight css %}
* Do not remove this line (it will not be displayed) 
{:toc}
{% endhighlight %}