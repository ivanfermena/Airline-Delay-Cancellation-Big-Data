---
layout: post
title:  "Retrasos en los distintos meses"
description: Que mes es el que acumula más retrasos
categories: batch
---



## Descripción
En este test se vamos a buscar cual es el mes del año que que tiene más retrasos en los 9 años de vuelos internos en EEUU.

## Ficheros
Son necearios los siguientes ficheros :


* `delayPerMonth.py`
* `2009-2018.csv`

## Ejecución
>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    spark-submit delayPerMonth.py


>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /delayPerMonth/*.csv


## Resultado

Partiendo del dataframe inicial se ejecuta una consulta que agrupa por mes todos los retrasos producidos. La salida generada es la siguiente: 


    +-----+------------+
    |Month|Cancelations|
    +-----+------------+
    |   12|       95190|
    |   11|       37784|
    |   10|       47058|
    |    9|       56817|
    |    8|       78847|
    |    7|       71662|
    |    6|       91087|
    |    5|       61889|
    |    4|       64034|
    |    3|       92317|
    |    2|      136908|
    |    1|      139616|
    +-----+------------+