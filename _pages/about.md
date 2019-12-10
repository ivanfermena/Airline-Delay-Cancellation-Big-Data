---
layout: page
title: About
permalink: /about/
show-in-menu: yes
---

## Descripción de proyecto

Proyecto de la asignatura llama "Cloud y Big Data" de la Facultad de Informática de la Universidad Complutense de Madrid en la que se pretende representar todos los conocimientos obtenidos a los largo de la asignatura. Se nos dan las bases para conocer y desarrollar en entornos cloud y big data, entendiendo cual es su pontencial y en que ocasiones hay que usar dichas tecnologias.
git satu
En particular en este proyecto se ha obtenido un dataset de vuelos nacionales de EEUU en la que aparece diferente información relativa a los retrasos y cancelaciones de estos vuelos. Se ha realizado un analisis estadistico de los datos con la finalidad de obtener patrones y comportamientos sobre estos retrasos y cancelaciones. La intención es que posteriormente se de una base solidad de analisis mas profundo para la obtencion de valor o toma de decisiones sobre el caso de uso.


## ¿Por qué usar procesamiento paralelo a gran escala?

Debido a la propia naturaleza de los datos y al problema que queremos resolver, obtendremos nuestra información de más de 30 Aeropuertos de Estados Unidos, los cuales tienen una media anual de entre 100.000 y 700.000 transacciones aéreas, lo que produce un alto volumen de información sobre los retrasos, cancelaciones e incidencias.
Si queremos realizar un análisis estadístico en tiempo real y de forma eficiente, la mejor técnica que podemos utilizar es Big Data, la complejidad de los datos, el volumen y la necesidad de un tratamiento de estos a una velocidad y en un tiempo coherentes con el problema que queremos resolver nos indican que el procesamiento en paralelo y a gran escala es una solución económicamente más asequible, que desempeña el objetivo de la forma más sencilla, rápida y menos compleja.

## Datos con los que contamos

Aunque se conoce que la finalidad del proyecto es realizar un prototipo a pequeña escala del caso de uso, contamos con un número significativo de datos como para ver el problema a resolver. Nuestros datos se basan en información de los vuelos cancelados o con retraso, en vuelos nacionales de los Estados Unidos,desde el año 2009 hasta 2018 y están proporcionados por la oficina de transportes. Se presentan en formato csv divididos por año con un peso total de 7 GB. 
Por cada dato, tenemos información referente al vuelo, identificándose aerolínea y vuelo. Además de los tiempos de vuelo desglosados en despegue, vuelo y aterrizaje. Con sus respectivos tiempos de retraso. En caso de que el vuelo se retrase, se desglosa las causas y se calcula en minutos. En caso de que se cancele o desvíe el vuelo, también se muestra la causa.
La mayoría de campos presenta una buena calidad, aunque no todos están exentos de datos nulos.

## Infraestructuras y aplicaciones usados

Para la realización de la práctica hemos usado como herramienta Apache Spark, tanto para la procesamiento en tiempo real como para batch, de este modo usamos una única herramienta unificada para ambos procesos. Debido a la cantidad de datos con la que disponemos, usaremos ejemplos mas pequeños de los datos para el procesamiento en batch y una seccion mas pequeña y preparada para el procesamiento en tiempo real, de este modo creamos todo el sistema necesario para la insercción de grandes cantidades de datos y reales.

Como infraestructura usaremos el procesamiento cloud de aws, ya que no contamos con infraestructura suficiente para hacer un cluster "On-Premises". Se tiene pensado el uso de las máquinas locales y código subido a github para realizar el desarrollo, debido a una mayor raidez de desarrollo en un ambiente en local y posteriormente desplegarlo en un cluster en aws. 

Usaremos como opción dada en aws el paquete de 4 vCPUs (m4.xlarge) de EMR, de este modo sabemos que tendremos el procesamiento necesario para la realización de estadísticas y gráficas que necesitamos. Así como el procesamiento en tiempo real.


<a class="github-button" href="https://github.com/sharu725/ashwath" data-style="mega" data-count-href="/sharu725/ashwath/stargazers" data-count-api="/repos/sharu725/ashwath#stargazers_count" data-count-aria-label="# stargazers on GitHub" aria-label="Star sharu725/ashwath on GitHub">Star</a>
<script async defer src="https://buttons.github.io/buttons.js"></script>