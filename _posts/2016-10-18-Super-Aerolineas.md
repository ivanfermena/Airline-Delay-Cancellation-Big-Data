---
layout: post
title:  "Aerolineas que superan sus retrasos"
description: Cuántos vuelos salen con retraso y llegan en hora
categories: batch
---


## Descripción

A lo largo de un día se producen miles de retrasos. Hemos estudiado qué pueden ser producidos por múltiples causas como la meteorología, la fecha del año o incluso por la gestión de la aerolinea.

En este apartado mostramos durante los nueve años de estudio cuántos vuelos que partían con un retraso inicial, finalmente han conseguido reducirlo y llegar a la hora preestablecida o incluso antes.  

## Ficheros

Los ficheros necesarios son los siguientes:
* `superAirlines.py`
* `2009-2018.csv`


## Ejecución
>Una vez situados en el directorio que contiene el dataset y el fichero de código ejecutamos el siguiente comando en la shell

    spark-submit superAirlines.py

>Nota: si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero .py  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /SuperAirlines/*.csv

## Resultado

Partiendo del dataframe que contiene todo el dataset inicial se ejecuta una consulta que agrupa todos los vuelos por aerolinea, que salieron con retraso de sus destinos pero llegaron antes de la hora de llegada establecida. La salida es la siguiente: 

    +--------+-------+
    |Airlines|  veces|
    +--------+-------+
    |      WN|1834906|
    |      DL| 794394|
    |      UA| 634504|
    |      AA| 604424|
    |      OO| 298017|
    |      EV| 258741|
    |      B6| 204681|
    |      US| 181306|
    |      MQ| 166467|
    |      CO| 118063|
    |      AS| 108380|
    |      FL|  83012|
    |      F9|  70279|
    |      9E|  54270|
    |      XE|  53467|
    |      NK|  38550|
    |      VX|  37861|
    |      YV|  37825|
    |      OH|  26240|
    |      NW|  23262|
    +--------+-------+
    only showing top 20 rows
