---
layout: post
title:  "Retrasos por día"
description:
categories: batch
---


## Descripción
En este test se compruebarán que cantidad de retrasos se producen cada día, esto nos permite analizar que tipo de razones pueden provocar dichos retrasos.

## Ficheros
Son necearios los siguientes ficheros :


* `delayPerDay.py`
* `2009-2018.csv`

## Ejecución
>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    spark-submit delayPerDay.py

>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /delayPerDay/*.csv

## Resultado

Partiendo del dataframe inicial se ejecuta una consulta que nos agrupa los retrasos en funcón del día. La salida generada es la siguiente.


    +------+-------------------+
    |Delays|               date|
    +------+-------------------+
    |   372|2009-01-01 00:00:00|
    |   474|2009-01-02 00:00:00|
    |   396|2009-01-03 00:00:00|
    |   421|2009-01-04 00:00:00|
    |   469|2009-01-05 00:00:00|
    |   470|2009-01-06 00:00:00|
    |   397|2009-01-07 00:00:00|
    |   411|2009-01-08 00:00:00|
    |   467|2009-01-09 00:00:00|
    |   316|2009-01-10 00:00:00|
    |   408|2009-01-11 00:00:00|
    |   455|2009-01-12 00:00:00|
    |   425|2009-01-13 00:00:00|
    |   377|2009-01-14 00:00:00|
    |   449|2009-01-15 00:00:00|
    |   476|2009-01-16 00:00:00|
    |   333|2009-01-17 00:00:00|
    |   362|2009-01-18 00:00:00|
    |   427|2009-01-19 00:00:00|
    |   402|2009-01-20 00:00:00|
    +------+-------------------+
    only showing top 20 rows

