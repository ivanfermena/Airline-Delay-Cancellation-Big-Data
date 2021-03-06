---
layout: post
title:  "Tipos de retrasos por meses"
description: Qué importancia tiene el momento del año en la causa del retraso de los vuelos
categories: batch
---



## Descripción
En este test se extraen los porcentajes que representan cada tipo de retraso que se da en los distintos meses del año. Esto nos permitirá analizar que tipo de factores relacionados con el momento del año pueden influir en las causas que provocan que un vuelo se retrase.

## Ficheros
Son necesarios los siguientes ficheros :


* `delayTypesPerMonth.py`
* `2009-2018.csv`

## Ejecución
>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    spark-submit delayTypesPerMonth.py


>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /delayTypesPerMonth/*.csv


## Resultado

Partiendo del dataframe inicial se ejecutan varias consultas que relacionan los tipos de retrasos con el momento del año en el que se producen. Calculando así el porcentaje de cada tipo de retraso durante el mes. La salida generada es la siguiente: 

        
    +-----+-------------+-------------+----------------+--------------+
    |Month|Airline_Delay|Weather_delay|Air_system_delay|Security_delay|
    +-----+-------------+-------------+----------------+--------------+
    |   12|        31.54|         3.51|           32.67|         32.27| <-- Percentages
    |    1|        30.23|         4.31|           34.68|         30.78|
    |    6|        30.58|         3.82|           32.46|         33.13|
    |    3|        30.77|         2.90|           34.36|         31.97|
    |    5|        29.96|         3.55|           34.43|         32.06|
    |    9|        30.50|         3.06|           36.04|         30.40|
    |    4|        29.99|         3.19|           34.86|         31.96|
    |    8|        30.78|         3.55|           32.87|         32.81|
    |    7|        30.77|         3.86|           31.98|         33.39|
    |   10|        31.19|         2.04|           35.14|         31.63|
    |   11|        31.54|         2.50|           34.73|         31.23|
    |    2|        29.88|         4.02|           35.38|         30.72|
    +-----+-------------+-------------+----------------+--------------+


