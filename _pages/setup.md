---
layout: page
title: SetUp
permalink: /setup/
show-in-menu: yes
---

# SetUp

Este proyecto se divide en dos partes:

- Análisis mediante Spark en modo batch
- Análisis mediante Spark Streaming de eventos en tiempo real

En cada una de las partes se explicaran todos los pasos necesarios para probar el código en vuestro ordenador, desde los pre-requisitos, las instalaciones y la ejecución de los programas .  

En esta guía se explica la manera de hacerlo en un sistema linux.

## Batch
Esta sección se centra en el análisis del dataset al completo y se compone de los siguientes programas/scripts :
- Retrasos en el aire ~ delay_per_journey
- Cancelaciones por dia ~ cancelledPerDay
- Cancelaciones por aerolinea ~ cancelledPerAirline
- Cancelaciones por lugar ~ cancelledPerCity
- Retrasos por dia ~ delayPerDay
- Retrasos por aerolinea ~ delayPerAirline
- Retrasos por lugar ~ delayPerCity
- Porcentaje de tipo de Retraso ~ DelayTypePerMonth
- Relacion distancia retraso ~ delayPerDistance
- Meses que mas retrasos tienen ~ delayPerMonth
- Peor y mejor día para volar ~ worstAndBestDayToFlight
- Peor y mejor més para volar ~ worstAndBestMonthToFlight

El nombre de los programas es el que se encuentra a la derecha en cada uno de los casos de uso seguido de una extensión **.py**
### Pre-requisitos
Para la ejecución de esta parte del código serán necesarios los siguientes elementos:

* Spark

>Puede acceder a la guía de instalación de Spark en modo local de clase desde este enlace.  [link](https://drive.google.com/file/d/1YX3-fyVV9fPQsqp6emV7tDa4-KoNcxva/view)

* Dataset

>Será necesario descargar en dataset 2009-2018 en formato csv disponible en este enlace.  [link](https://drive.google.com/file/d/1qd2dmv8isbE4zniFAYOMO0z2r4mokutk/view?usp=sharing)

* Código fuente 

>Será necesario descargar el código fuente de la parte batch del proyecto se encuentra en la carpeta **spark-batch** del repositorio.  [link](https://github.com/ivanfermena/code-airline-delay-cancellation-big-data)

* Dependencias

>Instalar el manager de paquetes de python
	
	sudo apt-get install python-pip

>Instalar el constructor de python thinker

	sudo apt-get install python-tk

>Instalar todos los paquetes necesarios
	
	pip install matplotlib
	pip install scikit-learn
	pip install pandas
	pip install plotly_express

### Salidas de los scripts
Si el usuario quiere obtener una salida en formato csv deberá descomentar la última linea de todos los scripts, la ejecución del programa será más lenta pero nos permitirá obtener los resultados de ejecución de una manera mas clara.

### Ejecución del código
Una vez hemos instalado Spark y hemos descagardo el dataset podremos proceder a la ejecución de los programas.  **Remarcamos** que los scripts y el dataset han de estar en el mismo directorio.

>Abrimos una shell del ordenador y accedemos al directorio donde se encuentra el código y el dataset

	cd <directorio>/spark-batch

>Para ejecutar un script, por ejemplo el de cancelados al día ejecutamos el siguiente comando

	spark-submit nombreDelFicher.py

>Ej:

	spark-submit cancelledPerDay.py

>Si hemos descomentado la línea que nos genera un fichero de salida ejecutamos la siguiente orden para visualizar el contenido

	cat /<nombreDelFicheroEjecutadoSinExtension>/*.csv

>Ej:

	cat /cancelledPerDay/*.csv

<script async defer src="https://buttons.github.io/buttons.js"></script>
