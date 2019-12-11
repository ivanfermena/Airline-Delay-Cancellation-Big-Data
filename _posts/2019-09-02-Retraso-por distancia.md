---
layout: post
title:  "Retrasos por Distancia"
description: 
categories: batch
---

![sample post]({{site.baseurl}}/images/image-2.png)




## Descrición

Los retrasos pueden ser producidas por diferentes causas, en este caso nos centramos en los vuelos y como influye su distancia con los retrasos. Lo que nos indicaría si el tiempo estimado esta bien calculado o no, estudiando los 9 años de vuelos internos en EEUU.
  

## Ficheros

Los ficheros necesarios son los siguientes:
* `delayPerDistance.py`
* `2009-2018.csv`


## Ejecución
>Una vez situados en el directorio que contiene el dataset y el fichero de código ejecutamos el siguiente comando en la shell

    spark-submit delayPerDistance.py

>Nota: si queremos generar un salida en formato csv se debe descomentar la última linea de código del fichero .py  
Para visualizar el contenido de la salida ejecutar el siguiente comando en la shell

    cat /DelayPerDistance/*.csv

## Resultado

Partiendo del dataframe que contiene todo el dataset inicial se ejecuta una consulta que agrupa todos los vuelos retrasados por su distancia y hace la media. La salida es la siguiente: 

    +-------------------+--------+
    |          avg_delay|distance|
    +-------------------+--------+
    | 1.3844700944386148|  4983.0|
    | 1.9664634146341464|  4963.0|
    | 1.4026974951830442|  4962.0|
    | 1.9060665362035225|  4817.0|
    |   6.27972027972028|  4678.0|
    | -3.703719008264463|  4502.0|
    | 1.7412587412587412|  4475.0|
    |  4.593335857629686|  4244.0|
    |  6.203327787021631|  4243.0|
    |-0.5984555984555985|  4213.0|
    |  8.067024128686327|  4184.0|
    |-2.5446104158255953|  3972.0|
    |  6.274344680346341|  3904.0|
    |  41.28865979381443|  3847.0|
    |  7.889309040907528|  3801.0|
    | 11.807727114514444|  3784.0|
    |  13.18918918918919|  3724.0|
    |  9.861519189158411|  3711.0|
    |  4.120376597175521|  3417.0|
    | -5.712248865845755|  3414.0|
    +-------------------+--------+