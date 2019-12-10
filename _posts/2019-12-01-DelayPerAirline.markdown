---
layout: post
title:  "Retrasos por aerolineas"
description:
categories: batch
---

# Retrasos en función de la aerolinea

## Descripción
En este test se compruebarán que aerolineas acumulan más retrasos en el total del histórico. Esto nos ayudará a la hora de encontrar factores clave, ya que podremos buscar las diferencias y similitudes que tienen las distintas aerolineas en función de la densidad de retrasos.

## Ficheros
Son necearios los siguientes ficheros :


* `delayPerAirline.py`
* `2009-2018.csv`

## Ejecución
>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    spark-submit delayPerAirline.py
>**Nota:** si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero **.py**  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /delayPerAirline/*.csv


## Resultado

Partiendo del dataframe inicial se ejecuta una consulta que nos agrupa por aerolineas los retrasos que han sufrido. La salida generada es la siguiente.

    +-------+-------+
    | Delays|Airline|
    +-------+-------+
    | 346515|     9E|
    |2505021|     AA|
    | 548166|     AS|
    | 975547|     B6|
    | 316274|     CO|
    |2437633|     DL|
    |1761113|     EV|
    | 401818|     F9|
    | 442689|     FL|
    |  37177|     G4|
    | 250666|     HA|
    |1234930|     MQ|
    | 220727|     NK|
    | 120352|     NW|
    | 240916|     OH|
    |2290032|     OO|
    |1625819|     UA|
    | 964503|     US|
    | 153326|     VX|
    |4767155|     WN|
    +-------+-------+
    only showing top 20 rows

