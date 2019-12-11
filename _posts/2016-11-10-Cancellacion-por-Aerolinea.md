---
layout: post
title:  "Cancelaciones por Aerolínea"
description: Cuantas cancelaciones hay por aerolínea en los últimos 9 años
categories: batch
---




## Descripción

Las cancelaciones pueden ser producidas por diferentes causas, en este caso nos centramos en que aerolineas son más propensas a cancelar vuelos y cuales no, estudiando los 9 años de cancelaciones en vuelos internos en EEUU.
  

## Ficheros

Los ficheros necesarios son los siguientes:
* `cancelledPerAirline.py`
* `2009-2018.csv`


## Ejecución
>Una vez situados en el directorio que contiene el dataset y el fichero de código ejecutamos el siguiente comando en la shell

    spark-submit cancelledPerAirline.py

>Nota: si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero .py  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /CancellationPerAirlines/*.csv

## Resultado

Partiendo del dataframe que contiene todo el dataset inicial se ejecuta una consulta que a grupa todos los vuelos cancelados por aerolinea. La salida es la siguiente: 

    +-------------+-------+
    |Cancellations|Airline|
    +-------------+-------+
    |        25797|     9E|
    |       108555|     AA|
    |        10796|     AS|
    |        43906|     B6|
    |         6142|     CO|
    |        62966|     DL|
    |       137042|     EV|
    |         7143|     F9|
    |        11732|     FL|
    |          769|     G4|
    |         1412|     HA|
    |       113693|     MQ|
    |        11511|     NK|
    |         1759|     NW|
    |        22623|     OH|
    |       114445|     OO|
    |        58635|     UA|
    |        36711|     US|
    |         3550|     VX|
    |       133587|     WN|
    +-------------+-------+