---
layout: post
title:  "Cancelaciones en función de las ciudades"
description:
categories: batch
---



## Descripción
En este test se compruebarán que cantidad de cancelaciones se producen por cada una de las ciudades de origen del buelo, de esta manera podemos estudiar como están relacionadas al zona geográfica y el clima con la causa de las cancelaciones.

## Ficheros
Son necearios los siguientes ficheros :


* `cancelledPerCity.py`
* `2009-2018.csv`

## Ejecución
>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    spark-submit cancelledPerCity.py

>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /cancelledPerCity/*.csv

## Resultado

Partiendo del dataframe inicial se ejecuta una consulta que nos ofrece la cantidad de cancelaciones que sufre una ciudad durante todos los años disponibles. La salida es la siguiente:


    +------------+------+
    |Cancelations|Origin|
    +------------+------+
    |         810|   ABE|
    |         609|   ABI|
    |        2277|   ABQ|
    |          85|   ABR|
    |         142|   ABY|
    |         105|   ACK|
    |         461|   ACT|
    |        1432|   ACV|
    |         334|   ACY|
    |          59|   ADK|
    |         436|   ADQ|
    |         765|   AEX|
    |         543|   AGS|
    |           2|   AKN|
    |        1780|   ALB|
    |         199|   ALO|
    |        1345|   AMA|
    |        1672|   ANC|
    |         116|   APN|
    |          96|   ART|
    +------------+------+
    only showing top 20 rows