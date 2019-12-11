---
layout: post
title:  "Tipos de retrasos en los distintos meses"
description:
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


    +----+-----+------------+
    |Year|Month|      Delays?|
    +----+-----+------------+
    |2011|   12|        3713|
    |2018|   12|        6752|
    |2009|   12|       14730|
    |2012|   12|        7970|
    |2010|   12|       19692|
    |2013|   12|       14747|
    |2015|   12|        8063|
    |2016|   12|        7464|
    |2017|   12|        5324|
    |2014|   12|        6735|
    |2011|   11|        3228|
    |2013|   11|        5082|
    |2012|   11|        5105|
    |2018|   11|        6254|
    |2015|   11|        4599|
    |2010|   11|        3755|
    |2017|   11|        1418|
    |2016|   11|        1310|
    |2009|   11|        2732|
    |2014|   11|        4301|
    +----+-----+------------+