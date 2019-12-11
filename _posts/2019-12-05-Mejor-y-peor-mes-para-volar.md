---
layout: post
title:  "El mejor y el peor mes para volar"
description: Pensado en viajar dentro EEUU, el mejor y peor més para coger un avión
categories: batch
---


## Descripción
En este test se vamos a mostrar como influye la ruta en los retrasos de los vuelos en los 9 años de vuelos internos en EEUU.

## Ficheros
Son necearios los siguientes ficheros :


* `worstAndBestMonthToFlight.py`
* `2009-2018.csv`

## Ejecución
>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    spark-submit worstAndBestMonthToFlight.py


>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /worstAndBestMonthToFlight/*.csv


## Resultado

Partiendo del dataframe inicial se ejecutan varias consultas y se mezclan entre ellas para generar un dataframe con toda la información de todos los meses de todos los años. De entre estos se busca el mes que menos incidencias registró y el que más. La salida es la siguiente: 

    +---------+-----+
    |Incidents|Month|
    +---------+-----+
    |  2500985|    6|
    |  1600872|   10|
    +---------+-----+