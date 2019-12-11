---
layout: post
title:  "Realización de estudio de correlaciones y aplicación de regresión lineal sencilla"
description: Análisis estadístico intentando averiguar si existe una correlación entre el origen y destino con la posible cancelación de un vuelo.
categories: machinelearning
---

## Descripcion:

En esta sección del proyecto se pretende averiguar si la unión de Origen-Destion esta correlacionada de alguna manera con la cancelación que se produce en los vuelos, y si no es así, buscar cuáles son las variables que ostentan mayor grado de correlación (que no dependan entre ellas) y aplicar un modelo de regresión lineal para intentar predecir futuros valores, siempre que ese valor sea lo suficientemente valioso. 

## Ficheros 

* `ml.py`
* `2009-2018.csv`

## Ejecución

>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    python ml.py

>En este caso, hemos aplicado técnicas de machine learning de la librería sklearn, para, en el caso de encontrar salidas con un cierto valor, conectarlo al procesamiento en paralelo, ya sea a partir de AWS en cloud, directamente con la herramienta de MachineLearning que da Apache Spark o estas dos opciones a la vez. Se ha aplicado esta librería basándonos en la experiencia previa del equipo, de este modo hemos agilizado este análisis previo.

Ahora veremos las secciones de código más importantes para facilitar la comprensión de cada pieza del código.

## Código

Primero se verán aquellas librerías que son necesarias para la aplicación de este código. Sklearn como se ha nombrado antes, matplotlib para la realización de gráficas, numpy y pandas para el procesamiento, OS para acceder a la estructura de directorios cuándo sea necesario desde código y por último "plotly.express", la cual sirve también para la realización de gráficas interactivas.

{% highlight python %}

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import mean_squared_error, r2_score

import matplotlib.pyplot as plt

import numpy as np 
import os 
import pandas as pd
import plotly.express as px

{% endhighlight %}

Omitiendo la limpieza de datos previa (eliminar NA, vacios...), lo primero que hay que hacer es convertir en variables categóricas las variables que no sean numéricas, es decir, el origen y el destino son valores como "ANL", un valor que dificulta los posteriores cálculos. Por eso lo que se hace es convertir en números los valores, "ANL" en 1, "DLO" en 2 ... El proceso para hacerlo es el que se muestra a continuación.

{% highlight python %}

cat_df_flights = df.select_dtypes(include=['object']).copy()

cat_df_flights = cat_df_flights[["ORIGIN","DEST"]]

labels = cat_df_flights['ORIGIN'].astype('category').cat.categories.tolist()

dicLabels = dict()

num = 0
for val in labels:
    dicLabels.setdefault(val, num)
    num = num + 1

df_cleaned = cat_df_flights.copy()

df_cleaned.replace( dicLabels, inplace=True)

df_cleaned['CANCELLED'] = df['CANCELLED']

{% endhighlight %}

Tras esto se muestran gráficas determinadas con la librería antes nombrada, "plotly.express" para el análisis de las correlaciones y del caso en particular para ver en detenimiento el origen y destino con la variable de cancelación.

>Gráficas interactivas de todas las relaciones entre variables(vista general)

![sample post]({{site.baseurl}}/images/grafica_grande.jpg)

>Gráficas de relaciones entre las variables a estudiar

![sample post]({{site.baseurl}}/images/grafica_peque.jpg)

Tras el estudio gráfico procedemos a entrenar nuestro modelo con las variables dictadas y la variable objetivo, dándonos cuenta que no obtenemos ni de cerca un valor con suficiente peso para el análisis. Algo que se podía intuir con las gráficas.

{% highlight python %}

modelo = LogisticRegression()

X = df_cleaned.loc[:,["ORIGIN","DEST"]]
y = df_cleaned["CANCELLED"]

print(X.shape)
print(y.shape)

#Entreno el modelo con los datos (X,Y)
modelo.fit(X, y)
 
#Podemos predecir usando el modelo
y_pred = modelo.predict(X)

{% endhighlight %}

## Resultado de primer modelo

{% highlight python %}

    Coeficiente beta1:  [ 0.00148963 -0.00230434]
    Error cuadratico medio: 0.02
    Estadistico R_2: -0.02

{% endhighlight %}

Visto los resultados del primer modelo se procede a analizar las variables que parecen mas significativas entre ellas graficamente y tras varias pruebas, mostramos aquel modelo que tiene mejores resultados de R_2. Siendo aún así poco valiosos para determinar que se puede predecir correctamente. Aunque no es bueno que el R_2 este sobreajustado, ni siquiera así, el resultado es bueno.

{% highlight python %}

modelo = LogisticRegression()

df_cleaned = df[["CRS_DEP_TIME","WHEELS_ON","WHEELS_OFF"]].dropna()

X = df_cleaned.loc[:,["WHEELS_ON","WHEELS_OFF"]]
y = df_cleaned["CRS_DEP_TIME"]

print(X.shape)
print(y.shape)

#Entreno el modelo con los datos (X,Y)
modelo.fit(X, y)

{% endhighlight %}

## Resultado de segundo modelo

{% highlight python %}

    Coeficiente beta1:  [-0.00112003 -0.06410115]
    Error cuadratico medio: 116702.73
    Estadistico R_2: 0.52

{% endhighlight %}

Como conclusión de la realización del modelo de regresión lineal hemos averiguado que este modelo carece de complejidad para obtener previsiones concluyentes sobre los datos que se tenían, para esto, sería interesante aplicar otros métodos como DeepLearning o KMeans, mucho más sotisficados.


