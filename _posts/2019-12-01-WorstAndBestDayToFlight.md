---
layout: post
title:  "EL mejor y el peor día para volar"
description:
categories: batch
---

# El mejor y el peor día para volar

## Descripción
En este test se calcula cual es mejor y el peor día del año basado en la cantidad de incidencias que ocupan cada uno de los dias del año.

## Ficheros
Son necearios los siguientes ficheros :


* `worstAndBestDayToFlight.py`
* `2009-2018.csv`

## Ejecución
>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    spark-submit worstAndBestDayToFlight.py

>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /worstAndBestDayToFlight/*.csv

## Resultado

Partiendo del dataframe inicial se ejecutan varias consultas y se mezclan entre ellas para generar un dataframe con toda la información de todos los días de todos los años. De entre estos se busca el día que menos incidencias registró y el que más. La salida es la siguiente: 

    +---------+-----+---+
    |Incidents|Month|Day|
    +---------+-----+---+
    |    30175|    7|  4| <-- Best day
    |    92478|    6| 23| <-- Worst day
    +---------+-----+---+
