---
layout: page
title: Documents
permalink: /documents/
show-in-menu: yes
---

COSAS QUE FALTAN:

- [ ] Punto dos las conclusiones/resultados que hemos sacado y otras soluciones (no se si existen)
- [ ] 

El proyecto tiene que ser capaz de justificar los siguientes apartados:

* Do not remove this line (it will not be displayed) 
{:toc}

# **Descripción de la necesidad de Big Data**

Nos encontramos antes un problema muy orientado a un procesamiento paralelo a gran escala, el caso de uso de la aviación siempre ha sido un foco principal del procesamiento a gran escala, tanto por la gran cantidad de datos que trata, como por las diferentes fuentes de datos que necesita analizar. Nuestro caso de uso solo se centra en vuelos nacionales dentro de EEUU, pero ya solo con eso tratamos cerca de entre 100.000 y 700.000 transacciones aéreas por año que se producen en cada uno de los 30 aeropuertos activos a día de hoy. Para realizar análisis estadísticos, transformaciones o agrupaciones de los diferentes datos es necesario una potencia de computo muy elevado y por ello nos aprovechamos de la ventaja que da el porcesamiento en paralelo a gran escala.

Además estos datos van creciendo cada año, tanto en complejidad como en volumen, lo que hace imprescindible un aumento comodo de esta potencia de procesamiento. Ademas de que se pueden tratar de sistemas críticos, aunque no sea en específico de nuestro caso de uso, el big data en aviación es sensible ya que tratamos con vidas de personas y nuestras decisiones pueden afectar a estas tanto directamente como indirectamente. Por todo esto es necesario que se pueda realizar un escalado horizontal de nuestro sistema pata aumentar la potencia de calculo y tener la posibilidad de gestionar caidas de nodos sin que se pierda información.

El Data Science, nos da la oportunidad de tomar decisiones y dar valor a los datos, para aquellas personas que tengan conocimientos de negocio del caso de uso puedan sacar valor de los datos analizados. El Big Data nos da esta opción pero con los problemas que nos da el procesamiento con grandes cantidades de datos, con variedad de datos amplia, dandonos amplia velocidad de procesamiento y puediendo conseguir la veracidad en los datos esperada.

Finalmente el procesamiento en paralelo se encuentra muy bien integrado con el procesamiento en cloud, gracias a la elasticidad que nos brinda adapandonos a la necesidad de computación que necesitamos en cada momento, procesamiento por demanda. Por tanto, con el uso de cloud para nuestro procesamiento obtenemos menos costes (evitando inversiones en infraestructura), rapidez, accesible desde cualquier sitio (diferentes dispositivos), comodidad (versiones del sistema, actualizaciones, seguridad...), personalizacion de espacios y seguridad.

# **Descripción de la solución y comparación con el trabajo existente sobre el problema.**

En el proyecto hemos analizado y procesado la mayoria de casos posibles sobre los vuelos nacionales de EEUU buscando diferentes informaciones relativas a los retrasos y cancelaciones de estos vuelos. Se ha realizado un analisis estadistico de los datos con la finalidad de obtener patrones y comportamientos sobre los datos. La intención es que posteriormente se de una base solidad de análisis más profundo para la obtencion de valor o toma de decisiones sobre el caso de uso. 

El problema en particular es la falta de un analisis de porque se producen estos retrasos y cancelaciones en EEUU, ademas como se veran en los ejemplos de la pagina web se pierden muchos minutos y vuelos por este motivo. Creemos que es algo que tratan las empresas a nivel privado pero no hemos encontrado sistemas abiertos que cumplan con el estandar de datos abiertos y presenten sus resultados. Las aerolineas pierden grandes cantidades de recursos debido a estos retrasos y cancelaciones, sin contar posibles denuncias de los clientes.

Para ello hemos provisto de analisis en dos formas principales, una en tiempo real y otra sobre datos historicos. 

Los analisis en batch estudian muchos aspectos de los datos. A continuación se muestran estos casos explicados con ago de detalle:

- **Retrasos en mismas rutas:** Analisis de los acumulativo de todos los retrasos agrupado por origen y destino, ordenado de menor a mayor y menos para saber tambien quellos vuelos que tienen menos retrasos, intentando estudiar tambien porque es debido y aplicarlo aquellos que tienen mas retrasos.
- **Retrasos en el aire:** Estudio sencillo que localiza que vuelos tienen los retrasos en el tiempo en el que se encuentra el avión en el aire, esto se realiza comparandolo con el tiempo estimado de vuelo.
- **Cancelaciones por dia:** Número de cancelaciones por día para ver si es un numero mas alto del esperado.
- **Cancelaciones por aerolinea** Número de cancelaciones por aerolinea para ver si este problema esta focalizado en una sola o se reparte entre todas.
- **Cancelaciones por lugar:** Número de cancelaciones dictada por lugar, importante debido a las diferencias que hay entre los lugares de EEUU por su tamaño tan grande.
- **Retrasos por dia:** Número total del retraso por día para ver si es un número mas alto del esperado y compararlo con otro días ya que puede ser un condicionante que afecte mucho. Por ejemplo, los días cercanos puede haber mucho mas retrasos debido a la mayor afluencia de gente en los vuelos.
- **Retrasos por aerolinea:** Número total del retraso por aerolinea para ver si este problema esta focalizado en una sola aerolinea o se reparte entre todas.
- **Retrasos por lugar:** Número del retraso dictada por lugar, importante debido a las diferencias que hay entre los lugares de EEUU por su tamaño tan grande.
- **Porcentaje de tipo de Retraso:** Análisis interesante sobre el tipo de retraso que se produce y asi conocer en que tipo de retraso focalizar una vez localizadas aquellas secciones más críticas de los datos (por ejemplo, que lugares tienen mas retrasos).
- **Relacion distancia retraso:** Estudio sobre el retraso de un vuelo y comparandolo con la distancia que tiene que recorrer ese vuelo, ya que no sabemos si esta directamente enlazado un mayor retraso en un vuelo si esta muy distanciado el origen con el destino.
- **Meses que mas retrasos tienen:** Queremos saber de manera ordeada cuales son los meses que tienen más retrasos en los vuelos.
- **Peor y mejor día para volar:** Analisis orientado a estudio de que días estan mejor o peor destinados para el cliente a volar por los problemas que surgen esos dias.
- **Peor y mejor més para volar:** Analisis orientado a estudio de que meses estan mejor o peor destinados para el cliente a volar por los problemas que surgen esos meses.

Con todos estos casos creemos que damos una base solida e información suficiente para la toma de decisiones y poder localizar donde estan los problemas para estudiar soluciones especificas. Por la parte de analisis en tiempo real se centra más en el analisis  acumulativo del retraso que lleva un origen y un destino en un dia, de esta forma se pueden tomar decisiones en tiempo real para intentar mejorar esta solución, es decir, si un determinado vuelo tiene mucho retraso se puede enviar peticiones para que se ajusten mas los tiempos a dicho vuelo y asi intentar corregir este retraso o que por lo menos no aumente.

A parte, realizamos también un modelo donde se pretence averiguar si la unión de Origen-Destion esta correlada de alguna manera con la cancelacion que se produce en los vuelos, si no es asi, búscar cuales son las variables que estan mas fuertemente correladas (que no dependan entre ellas) y aplicar un modelo de regresión lineal para intentar predecir futuros valores, siempre que ese valor sea lo suficientemente valioso.

## Resultados y conclusiones

EN referente a la sección de la realización del modelo de regresión lineal hemos averiguado que este modelo no es suficiente complejo para obtener previsiones concluyentes sobre los datos que se tenian, para esto sería interesante aplicar otros métodos como DeepLearning o KMeans, mucho mas sotisficados.

# **Descripción detallada de su modelo y / o datos: de dónde vino, cómo lo adquirió, qué significa, etc.**

Aunque se conoce que la finalidad del proyecto es realizar un prototipo a pequeña escala del caso de uso, contamos con un número significativo de datos como para ver el problema a resolver. Nuestros datos se basan en información de los vuelos cancelados o con retraso, en vuelos nacionales de los Estados Unidos, desde el año 2009 hasta 2018 y están proporcionados por la ![oficina de transportes](https://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time). Se presentan en formato csv divididos por año con un peso total de 7 GB. Por cada dato, tenemos información referente al vuelo, identificándose aerolínea y vuelo. Además de los tiempos de vuelo desglosados en despegue, vuelo y aterrizaje. Con sus respectivos tiempos de retraso. En caso de que el vuelo se retrase, se desglosa las causas y se calcula en minutos. En caso de que se cancele o desvíe el vuelo, también se muestra la causa. A continuación se explica detenidamente cada campo del dataset para un mayor entendimiento:

![]({{site.baseurl}}/images/dataset1.png)

![]({{site.baseurl}}/images/dataset2.png)

![]({{site.baseurl}}/images/dataset3.png)

![]({{site.baseurl}}/images/dataset4.png)

La mayoría de campos presenta una buena calidad, aunque no todos están exentos de datos nulos. Por tanto, se realizó un analisis de los datos y se eliminaron aquellos que podian afectar negativa a los analisis. Aunque la calidad de los datos es buena, la manera de tratar campos no usados en la sección de cancelaciones es a partir de nulos, lo que implica un trato especifico para estos casos.

# **Descripción técnica de la aplicación paralela, modelos de programación, plataforma e infraestructura.**



# **Enlaces al repositorio con código fuente, conjuntos de datos de evaluación y casos de prueba**



# **Descripción técnica del diseño del software, línea de base del código, dependencias, cómo usar el código y el sistema y el entorno necesarios para reproducir sus pruebas.**



# **Evaluación del rendimiento (aceleración, rendimiento, escalado débil y fuerte) y discusión sobre los gastos generales y las optimizaciones realizadas**



# **Discusión final sobre los objetivos alcanzados, las mejoras sugeridas, las lecciones aprendidas, el trabajo futuro, las ideas interesantes ...**



# **Citaciones**