---
layout: post
title:  "Cancelaciones por día"
description: El número de cancelaciones que puede haber en un día en todo el tráfico interno de EEUU
categories: batch
---




## Descripción

Las cancelaciones pueden ser producidas por diferentes causas, en este caso nos centramos en que día del año es más propenso a cancelar vuelos y cuales no, estudiando los 9 años de cancelaciones en vuelos internos en EEUU.
  

## Ficheros

Los ficheros necesarios son los siguientes:
* `cancelledPerDay.py`
* `2009-2018.csv`


## Ejecución
>Una vez situados en el directorio que contiene el dataset y el fichero de código ejecutamos el siguiente comando en la shell

    spark-submit cancelledPerDay.py

>Nota: si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero .py  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /CancellationPerDay/*.csv

## Resultado

Partiendo del dataframe que contiene todo el dataset inicial se ejecuta una consulta que a grupa todos los vuelos cancelados por el dia del año. La salida es la siguiente: 

    +------------+-------------------+
    |cancelations|               date|
    +------------+-------------------+
    |         158|2009-01-01 00:00:00|
    |         213|2009-01-02 00:00:00|
    |         257|2009-01-03 00:00:00|
    |         249|2009-01-04 00:00:00|
    |         315|2009-01-05 00:00:00|
    |         391|2009-01-06 00:00:00|
    |         534|2009-01-07 00:00:00|
    |         335|2009-01-08 00:00:00|
    |         456|2009-01-09 00:00:00|
    |         663|2009-01-10 00:00:00|
    |         298|2009-01-11 00:00:00|
    |         555|2009-01-12 00:00:00|
    |         355|2009-01-13 00:00:00|
    |         567|2009-01-14 00:00:00|
    |         570|2009-01-15 00:00:00|
    |         367|2009-01-16 00:00:00|
    |         128|2009-01-17 00:00:00|
    |         281|2009-01-18 00:00:00|
    |         244|2009-01-19 00:00:00|
    |         254|2009-01-20 00:00:00|
    +------------+-------------------+
    only showing 20 rows