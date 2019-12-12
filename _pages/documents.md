---
layout: page
title: Documents
permalink: /documents/
show-in-menu: yes
---

COSAS QUE FALTAN:

- [ ] Punto dos las conclusiones/resultados que hemos sacado y otras soluciones (no se si existen)
- [ ] Seccion de citaciones.
- [ ] Ampliar lo necesario, revisar y exportar a pdf

El proyecto tiene que ser capaz de justificar los siguientes apartados:

* Do not remove this line (it will not be displayed) 
{:toc}

# **Definición del proyecto**

Proyecto de la asignatura llama “Cloud y Big Data” de la Facultad de Informática de la Universidad Complutense de Madrid en la que se pretende representar todos los conocimientos obtenidos a los largo de la asignatura. Se nos dan las bases para conocer y desarrollar en entornos cloud y big data, entendiendo cual es su pontencial y en que ocasiones hay que usar dichas tecnologias. En particular en este proyecto se ha obtenido un dataset de vuelos nacionales de EEUU en la que aparece diferente información relativa a los retrasos y cancelaciones de estos vuelos. Se ha realizado un analisis estadistico de los datos con la finalidad de obtener patrones y comportamientos sobre estos retrasos y cancelaciones. La intención es que posteriormente se de una base solidad de analisis más profundo para la obtencion de valor o toma de decisiones sobre el caso de uso.

# **Descripción de la necesidad de Big Data**

Nos encontramos ante un problema muy orientado a un procesamiento paralelo a gran escala. El caso de uso de la aviación siempre ha sido un foco principal del procesamiento a gran escala, tanto por la gran cantidad de datos que trata, como por las diferentes fuentes de datos que necesita analizar. Nuestro caso de uso sólo se centra en vuelos nacionales dentro de EEUU, pero ya sólo con esto, tratamos cerca de entre 100.000 y 700.000 transacciones aéreas por año que se producen en cada uno de los 30 aeropuertos activos a día de hoy. Para realizar análisis estadísticos, transformaciones o agrupaciones de los diferentes datos es necesaria una potencia de cómputo muy elevada y por ello nos aprovechamos de la ventaja que da el procesamiento en paralelo a gran escala.

Además estos datos van creciendo cada año, tanto en complejidad como en volumen, lo que hace imprescindible un escalado cómodo de esta potencia de procesamiento. Además de que se pueden tratar de sistemas críticos, aunque no sea en específico de nuestro caso de uso, el Big Data en aviación es sensible, ya que tratamos con vidas de personas y nuestras decisiones pueden afectar a éstas tanto directamente como indirectamente. Por todo ello, es necesario que se pueda realizar un escalado horizontal de nuestro sistema para aumentar la potencia de cálculo y tener la posibilidad de gestionar caídas de nodos sin que se pierda información.

El Data Science, nos da la oportunidad de tomar decisiones y dar sentido a los datos, para que, aquellas personas que tengan conocimientos de negocio del caso de uso puedan sacar valor de los datos analizados. El Big Data nos da esta opción pero con los problemas que conlleva el procesamiento con grandes cantidades de datos, con variedad de datos amplia, dándonos gran velocidad de procesamiento y pudiendo conseguir la veracidad en los datos esperada.

Finalmente el procesamiento en paralelo, se encuentra muy bien integrado con el procesamiento en cloud, gracias a la elasticidad que nos brinda adaptándose a la necesidad de computación que necesitamos en cada momento, gracias al procesamiento por demanda. Por tanto, con el uso de cloud para nuestro procesamiento, obtenemos menos costes (evitando inversiones en infraestructura), rapidez, accesibilidad desde cualquier plataforma, comodidad (versiones del sistema, actualizaciones, seguridad...), personalización de espacios y seguridad.

# **Descripción de la solución y comparación con el trabajo existente sobre el problema.**

En el proyecto hemos analizado y procesado la mayoría de casos posibles sobre los vuelos nacionales de EEUU buscando diferentes informaciones relativas a los retrasos y cancelaciones de estos vuelos. Se ha realizado un análisis estadístico de los datos con la finalidad de obtener patrones y comportamientos sobre los datos. La intención es que posteriormente se de una base solida de análisis más profundo para la obtención de valor o la toma de decisiones sobre el caso de uso. 

El problema en particular es la falta de un análisis del por qué se producen estos retrasos y cancelaciones en EEUU, además cómo se verá en los ejemplos de la página web se pierden muchos minutos y vuelos por este motivo. Creemos que es algo que tratan las empresas a nivel privado pero no hemos encontrado sistemas abiertos que cumplan con el éstandar de datos abiertos y presenten sus resultados. Las aerolíneas pierden grandes cantidades de recursos debido a estos retrasos y cancelaciones, sin contar posibles reclamaciones de los clientes.

Para ello hemos provisto de análisis en dos formas principales, una en tiempo real y otra sobre datos históricos. 

Los análisis en Batch estudian muchos aspectos de los datos. A continuación se muestran estos casos explicados con algo de detalle:

- **Retrasos en mismas rutas:** Análisis de los retrasos acumulados, agrupado por origen y destino, ordenado de menor a mayor para saber también aquellos vuelos que tienen menos retrasos, intentando estudiar a qué es debido y aplicarlo a aquellos que tienen más retrasos.
- **Retrasos en el aire:** Estudio sencillo que localiza que vuelos tienen los retrasos en el tiempo en el que se encuentra el avión en el aire, esto se realiza comparándolo con el tiempo estimado de vuelo.
- **Cancelaciones por dia:** Número de cancelaciones por día para ver si es un numero más alto del estimado.
- **Cancelaciones por aerolinea** Número de cancelaciones por aerolínea para ver si este problema esta focalizado en una sola o se reparte entre todas.
- **Cancelaciones por lugar:** Número de cancelaciones dictadas por lugar, importante debido a las diferencias que hay entre los lugares de EEUU por su gran extensión territorial.
- **Retrasos por dia:** Número total del retraso por día para ver si es un número más alto del esperado y compararlo con otro días ya que puede ser un condicionante que afecte mucho. Por ejemplo, los días cercanos puede haber muchos más retrasos debido a la mayor afluencia de gente en los vuelos.
- **Retrasos por aerolinea:** Número total del retraso por aerolínea para ver si este problema esta focalizado en una sola aerolínea o se reparte entre todas.
- **Retrasos por lugar:** Número de retrasos dictados por lugar, importante debido a las diferencias que hay entre los lugares de EEUU por su gran extensión territorial.
- **Porcentaje de tipo de Retraso:** Análisis interesante sobre el tipo de retraso que se produce y así conocer en qué tipo de retraso focalizar una vez localizadas aquellas secciones más críticas de los datos (por ejemplo, que lugares tienen más retrasos).
- **Relación distancia-retraso:** Estudio sobre el retraso de un vuelo y comparándolo con la distancia que tiene que recorrer ese vuelo, ya que no sabemos si esta directamente enlazado un mayor retraso en un vuelo si esta muy distanciado el origen con el destino.
- **Meses que mas retrasos tienen:** Queremos saber de manera ordenada cuáles son los meses que tienen más retrasos en los vuelos.
- **Peor y mejor día para volar:** Análisis orientado a estudio de que días están mejor o peor destinados para el cliente a volar por los problemas que surgen esos días.
- **Peor y mejor mes para volar:** Análisis orientado a estudio de que meses están mejor o peor destinados para el cliente a volar por los problemas que surgen esos meses.

Con todos estos casos creemos que damos una base sólida e información suficiente para la toma de decisiones y poder localizar donde estan los problemas para estudiar soluciones específicas. Por la parte de análisis en tiempo real nos centramos más en el análisis del retraso acumulado que lleva un origen y un destino en un día, de esta forma se pueden tomar decisiones en tiempo real para intentar mejorar esta solución, es decir, si un determinado vuelo tiene mucho retraso se puede enviar peticiones para que se ajusten más los tiempos a dicho vuelo y así intentar corregir este retraso o que por lo menos no aumente.

A parte, realizamos también un modelo, en el que se pretende averiguar si la unión de Origen-Destino está correlacionada de alguna manera con la cancelación que se produce en los vuelos,y si no es así, buscar cuáles son las variables que ostentan mayor grado de correlación (que no dependan entre ellas) y aplicar un modelo de regresión lineal para intentar predecir futuros datos, siempre sean lo suficientemente valiosos.

## Resultados y conclusiones

En referencia a la sección de la realización del modelo de regresión lineal hemos averiguado que este modelo carece de complejidad para obtener previsiones concluyentes sobre los datos que se tenían, para esto, sería interesante aplicar otros métodos como DeepLearning o KMeans, mucho más sotisficados.

# **Descripción detallada de su modelo y / o datos: de dónde vino, cómo lo adquirió, qué significa, etc.**

Aunque se conoce que la finalidad del proyecto es realizar un prototipo a pequeña escala del caso de uso, contamos con un número significativo de datos como para ver el problema a resolver. Nuestros datos se basan en información de los vuelos cancelados o con retraso, en vuelos nacionales de los Estados Unidos, desde el año 2009 hasta 2018 y están proporcionados por la [oficina de transportes](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time). Se presentan en formato csv divididos por año con un peso total de 7 GB. Por cada dato, tenemos información referente al vuelo, identificándose aerolínea y vuelo. Además de los tiempos de vuelo desglosados en despegue, vuelo y aterrizaje. Con sus respectivos tiempos de retraso. En caso de que el vuelo se retrase, se desglosa las causas y se calcula en minutos. En caso de que se cancele o desvíe el vuelo, también se muestra la causa. A continuación se explica detenidamente cada campo del dataset para un mayor entendimiento:

![]({{site.baseurl}}/images/dataset1.png)

![]({{site.baseurl}}/images/dataset2.png)

![]({{site.baseurl}}/images/dataset3.png)

![]({{site.baseurl}}/images/dataset4.png)

La mayoría de campos presenta una buena calidad, aunque no todos están exentos de datos nulos. Por tanto, se realizó un analisis de los datos y se eliminaron aquellos que podian afectar negativamente a los análisis. Aunque la calidad de los datos es buena, la manera de tratar campos no usados en la sección de cancelaciones es a partir de nulos, lo que implica un trato específico para estos casos.

Aunque contamos con muchos datos no tenemos una entrada de datos por vía streaming, por ello. La principal problemática que hemos encontrado a la hora de analizar en tiempo real los datos, es justamente, la falta de una fuente de datos en tiempo real. Sabemos que en el caso de uso que hemos elegido se analizan muchos datos en tiempo real y por eso es necesario realizar este apartado.

Para ello hemos extraído una parte de los datos y hemos creado un socket que envía datos cada cierto tiempo por dicho canal, de este modo somos capaces de obtener por Spark Streaming los datos y analizar todo lo necesario. El socket lee un "csv" dado por nosotros y envía por esa comunicación una línea cada vez. En nuestro caso, ya que teníamos el socket abierto nos ha parecido interesante devolver los datos analizados al cliente (proveedor de líneas) para completar la comunicación.

# **Descripción técnica de la aplicación paralela, modelos de programación, plataforma e infraestructura.**

Para la realización de la práctica hemos usado como herramienta Apache Spark, tanto para el procesamiento en tiempo real como para Batch, de este modo, usamos una herramienta unificada para ambos procesos. Debido a la cantidad de datos con la que disponemos, usaremos ejemplos más pequeños de los datos para el procesamiento en Batch y una sección más pequeña y preparada para el procesamiento en tiempo real, de este modo creamos todo el sistema necesario para la insercción de grandes cantidades de datos y reales.

Como infraestructura usaremos el procesamiento cloud de AWS, ya que no contamos con infraestructura suficiente para hacer un clúster “On-Premise”. Se tiene pensado el uso de las máquinas locales con varios cores y código subido a github para realizar el desarrollo, debido a una mayor rapidez de desarrollo en un ambiente en local y posteriormente desplegarlo en un clúster en AWS. Como se especificará en otras secciones es importante el uso de la potencia del cloud computing en el caso de usar todos los datos provistos en la versión final debido a la falta de computación en ámbito local y el tiempo elevado que necesita para terminar el proceso especificado.

Usaremos como opción dada en AWS, el paquete de 4 vCPUs (m4.xlarge) de EMR, de este modo sabemos que tendremos el procesamiento necesario para la realización de estadísticas y gráficas que necesitamos. En el caso de streaming hemos usado esta misma distribución de EMR pero se podría plantear aumentarlo en pruebas diarias, las cuales no hemos realizado, pero es posible que al ser una ventana diaria, en las últimas horas del día el procesamiento sea muy grande y pueda llegar a ser necesaria mayor capaciad. Para este último caso se estima que EMR de AWS es la mejor elección debido a la elasticidad que ofrece.

# **Enlaces al repositorio con código fuente, conjuntos de datos de evaluación y casos de prueba**

El código se encuentra a lo largo de las explicaciones de cada uno de los casos, así como una explicación de cómo probar el caso en particular, librerías y dataset necesarios para obtener la misma salida que mostramos. Aún así las explicaciones de cada caso no están completas y se aconseja coger el código del repositorio principal.

Página web donde están todos los casos explicados: [GitHub Page](https://ivanfermena.github.io/airline-delay-cancellation-big-data/)
Repositorio de GitHub: [GitHub](https://github.com/ivanfermena/code-airline-delay-cancellation-big-data/)
Enlace donde se encuentran los datos para los casos: [Drive](https://drive.google.com/file/d/1qd2dmv8isbE4zniFAYOMO0z2r4mokutk/view?usp=sharing)
Plataforma de datos inicial donde se pueden extraer más datos: [oficina de transportes](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time)

# **Descripción técnica del diseño del software, línea de base del código, dependencias, cómo usar el código y el sistema y el entorno necesarios para reproducir sus pruebas.**

Este proyecto se divide en dos partes ya explicadas en puntos determinados.

- Análisis mediante Spark en modo batch
- Análisis mediante Spark Streaming de eventos en tiempo real

En todas los analisis realizados se tiene una descripción detallada en la página web donde se explicaran todos los pasos necesarios para probar el código en vuestro ordenador, desde los pre-requisitos, las instalaciones y la ejecución de los programas. En esta sección se explica la manera de hacerlo en un sistema linux, asi como los proramas/librerias necesarias para su instalación y prueba.

## Batch
Esta sección se centra en el análisis del dataset al completo y se compone del siguientes programas/scripts :
- Retrasos en mismas rutas ~ delay_per_journey.py
- Retrasos en el aire ~ delay_per_journey.py
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

>Será necesario descargar el código fuente de la parte batch del proyecto se encuentra en la carpeta **spark-batch** del repositorio.  [link](https://github.com/ivanfermena/code-airline-delay-cancellation-big-data/)

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

    Aun asi es importante que en cada uno de los ejemplos se vaya a cada sección en la página web ya que además de una explicación mas detallada dedependencias y instalaciones necesarias.

### Salidas de los scripts
Si el usuario quiere obtener una salida en formato csv deberá des-comentar la última linea de todos los scripts, la ejecución del programa será mas lenta pero nos permitirá obtener los resultados de ejecución de una manera mas clara.

### Ejecución del código
Una vez hemos instalado Spark y hemos descagardo el dataset podremos proceder a la ejecución de los programas.  **Remarcamos** que los scripts y el dataset han de estar en el mismo directorio.

>Abrimos una shell del ordenador y accedemos al directorio donde se encuentra el código y el dataset

	cd <directorio>/spark-batch

>Para ejecutar un script, por ejemplo el de cancelados al día ejecutamos el siguiente comando

	spark-submit nombreDelFicher.py

>Ej:

	spark-submit cancelledPerDay.py

>Si hemos des-comentado la linea que nos genera un fichero de salida ejecutamos la siguiente orden para visualizar el contenido

	cat /<nombreDelFicheroEjecutadoSinExtension>/*.csv

>Ej:

	cat /cancelledPerDay/*.csv

Finalmente como entornos no es mas necesario que la linea de comandos de linux y si es requerido, un editor de texto para poder visualizar correctamente el código, pero no es necesaria la instalación de más entornos que los que nombramos con anterioridad.

# **Evaluación del rendimiento (aceleración, rendimiento, escalado débil y fuerte) y discusión sobre los gastos generales y las optimizaciones realizadas**

Lo primero que se nos plantea a la hora de desarrollar el trabajo son las necesidades que tiene nuestra aplicación. En este caso nos encontramos con una aplicación que realiza procesamiento de datos a gran escala, lo que significa que cuantos más datos existan mayor será el tiempo requerido para la ejecución del software. Por lo tanto nuestra principal necesidad se basa en los recursos que usaremos para procesar todos estos datos.

Debido al proceso de desarrollo realizado durante el proyecto no se han tenido problemas de rendimiento muy elevados. Hemos usado ejemplos del dataset con suficientes datos significativos para hacer los casos pero sin que se perdiera mucho tiempo en cada procesamiento o consulta. El tamaño de este dataset de prueba ha sido diferente dependiendo del nivel de computo y cores que tenia cada ordenador personal de los miembros del equipo, pero finalmente si se unificaron estas conclusiones dando una solucion final con el ordenador mas potente y usando la cantidad de cores máxima para provechar el procesamiento paralelo que nos brinda este paradigma. 

Esta necesidad nos hace pensar en el tipo de infraestructura que vamos a utilizar, y aquí no hay duda. Scale out es un término que hace referencia a la capacidad de crecimiento horizontal, es decir, no es la capacidad lo que importa sino el número de recursos con el que se cuenta. Si aplicamos esta propiedad a nuestro proyecto, lo que necesitamos es crecer en la cantidad de hardware y no en la potencia de este.

Aquí es donde entra AWS, la plataforma que nos brinda la oportunidad de conseguir esa elasticidad. Con una infraestructura cloud podemos crear instancias de máquinas remotas que nos permiten aumentar el número de ordenadores que utilizamos para el procesado de datos, es decir, podemos utilizar 20 maquinas para distribuir el trabajo de procesado entre todas ellas.

Realizaremos una ejecución de un script del proyecto en local y otra utilizando AWS. Hay que tener en cuenta que en los dos ejemplos utilizamos Spark como modelo de programación, lo que nos permite en cierta medida mejorar el rendimiento del programa incluso en una máquina individual.

En la prueba se ejecutará uno de los casos del proyecto, en concreto el script "delaysTyperPerMonth". Al realizar la prueba en diferentes máquinas el mejor rendimiento obtenido es de una duración de **7 minutos y 15 segundos**. En otros casos llegaba a durar mas de 15 minutos la ejecución o incluso no acabar y saltar un probema de memoria.

Para hacer la prueba en AWS levantamos un cluster con Spark, en este cluster utilizaremos Hadoop como sistema de ficheros compartido. EL cluster tiene 15 instancias m4xlarge con 4 cores cada una, es decir 56 cores disponibles como workers y 4 como master. La ejecución del script en el peor de los lanzamiento realizados es de un tiempo de **1 minuto y 30 segundos**.

Como conclusión podemos dictar claramente que obtenemos una mejora sustancial en la ejecución aprovechandonos del cloud computing, ya que nos disminuye sustancial mente el tiempo de procesamiento gracias a su elasticidad traducida en escalado horizontal de manera simple y sencilla para el cliente.

# **Discusión final sobre los objetivos alcanzados, las mejoras sugeridas, las lecciones aprendidas, el trabajo futuro, las ideas interesantes ...**

Como conclusión 

A la hora de plantear mejoras sobre nuestro proyecto sería interesante conocer, qué es justo lo que necesita el negocio, para no lanzar hipotésis poco fundamentadas, aunque bajo nuestro juicio puede que sea un problema ya estudiado por la industria. Sabemos que el dataset es completo y permite realizar grandes estudios sobre el caso de uso, pero sería interesante cruzarlo con otros datasets que tengan datos diferentes de las propias aerolíneas que pueden tener información más detallada de por qué surgen estos retrasos y cancelaciones.

Por otra parte pensamos que se podría dar más valor al análisis en tiempo real ya que sería interesante ingresar alertas cuando se superan determinados umbrales para un mayor control de la situación o realizar análisis de otras variables como la cancelación en tiempo real. Además consideramos que el análisis de modelos de machine learning con regresión lineal se queda muy limitado y nos hubiera gustado aplicar modelos más complejos como Deep Learning o KMeans, que podrían expresar resultados más precisos. Si se consiguiera esto, se podría hacer previsiones del tiempo de retraso que va a tener un vuelo a partir de unos parámetros, algo importante para poder anticiparse en la toma de decisiones y poder evitarlo.

En el caso determinado del procesamiento en streaming no nos hemos visto limitados por aquellos problemas reales del analisis en tiempo real, como podría ser la latencia. Sería algo interesante de estudiar en un determinado momento futuro llevando una extensión de la parte de streaming a cloud y estudiar como afecta esa latencia al rendimiento del modelo.

Aún con todo lo que se puede ampliar el proyecto, estamos más que satisfechos con los conocimientos adquiridos, ya que se ha constituido una buena aproximación a las tecnologías que han permitido asentar las bases teóricas recibidas durante el curso. Nos permite poder tomar decisiones de cuando es determinado el uso del Big Data y cloud, justificando correctamente su uso, asi como sus ventajas y desventajas.

# **Citaciones**

