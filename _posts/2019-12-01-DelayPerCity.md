---
layout: post
title:  "Retrasos por ciudad"
description:
categories: batch
---

# Retrasos en función de las ciudades

## Descripción
En este test se compruebarán que cantidad de retrasos se producen por cada una de las ciudades de origen del buelo, de esta manera podemos estudiar como están relacionadas al zona geográfica y el clima con la causa de los retrasos.

## Ficheros
Son necearios los siguientes ficheros :


* `delayPerCity.py`
* `2009-2018.csv`

## Ejecución
>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    spark-submit delayPerCity.py

>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /delayPerCity/*.csv

## Resultado

Partiendo del dataframe inicial se ejecuta una consulta que nos ofrece la cantidad de retrasos que sufre una ciudad durante todos los años disponibles. La salida es la siguiente:


    +------+------+
    |Delays|Origin|
    +------+------+
    | 10212|   ABE|
    |  6360|   ABI|
    | 95222|   ABQ|
    |  1453|   ABR|
    |  3411|   ABY|
    |  1783|   ACK|
    |  3527|   ACT|
    | 10015|   ACV|
    |  5549|   ACY|
    |   451|   ADK|
    |  1773|   ADQ|
    | 10842|   AEX|
    | 12313|   AGS|
    |   275|   AKN|
    | 31933|   ALB|
    |  1412|   ALO|
    | 20039|   AMA|
    | 55030|   ANC|
    |  1085|   APN|
    |   451|   ART|
    +------+------+
    only showing top 20 rows