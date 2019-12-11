---
layout: post
title:  "Aerolineas que superan sus retrasos"
description: 
categories: batch
---

![sample post]({{site.baseurl}}/images/image-2.png)


# Aerolineas que superan sus retrasos

## Descripcion

A lo largo de un día se producen miles de retrasos, hemos estudiado que pueden ser producidos por multiples causas como la meteorología, la fecha del año o incluso por la gestión de la aerolinea.

En este apardado mostramos durante los nueve años de estudio cuantos vuelos que partian con unretraso inicial, finalmente han conseguido reducirlo y llegar a la hora preestablecida o incluso antes.  

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

Partiendo del dataframe que contiene todo el dataset inicial se ejecuta una consulta que a grupa todos los vuelos por aerolinea, que salieron con retraso de sus destinos pero llegaron antes de la hora de llegada establecida. La salida es la siguiente: 

    +---------+-----+---+
    |Incidents|Month|Day|
    +---------+-----+---+
    |    30175|    7|  4| <-- Best day
    |    92478|    6| 23| <-- Worst day
    +---------+-----+---+