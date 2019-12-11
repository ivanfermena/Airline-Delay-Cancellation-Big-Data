---
layout: post
title:  "Realización de estudio de correlaciones y aplicación de regresión lineal sencilla"
description: Analisis estadistico intentando averiguar si existe una correlacion entre el origen y destino con la posibl cancelacion de un vuelo.
categories: machinelearning
---

## Descripcion:

En esta sección del proyecto se pretence averiguar si la unión de Origen-Destion esta correlada de alguna manera con la cancelacion que se produce en los vuelos, si no es asi, bscar cuales son las variables que estan mas fuertemente correladas (que no dependan entre ellas) y aplicar un modelo de regresión lineal para intentar predecir futuros valores, siempre que ese valor sea lo suficientemente valioso. 

## Ficheros 

* `ml.py`
* `2009-2018.csv`

## Ejecución

>Una vez situados en el directorio que contiene el **dataset** y el **fichero de código** ejecutamos el siguiente comando en la shell

    python ml.py

>En este caso, hemos aplicado técnicas de machine learning de la libreria sklearn, para en el caso de que salieran valores con un cierto valor conectarlo al procesamiento en paralelo, ya sea a partir de aws en cloud, directamente con la herramienta de MachineLearning que da Apache Spark o estas dos opciones a la vez. Se ha aplicado previamente en esta libreria por conocimientos de su uso de los miembros del equipo, de este modo se agilizaria este analisis previo.

Ahora veremos las secciones de código más importantes para un entendimiento lo mas completo de cada parte del código.

## Código

Primero se veran aquellas librerias que son necesarias para la aplicación de este código. Entre estas librerias se encuentran varias de sklearn como se ha nombrado antes, matplotlib para la realización de gráficas, numpy y pandas para el procesamiento, os para acceder a la estructura de directorios cuando sea necesario desde código y por último "plotly.express", la cual sirve también para la realización de gráficas interactivas.

Cabe destacar que muchas de estas librerias en el código mostrado a continuación no aparecen pero si han sido muy importantes para el estudio y transformaciones de los datos.

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

Omitiendo la limpieza de datos previa (eliminar NA, vacios...) lo primero que hay que hacer es convertir en variables categoricas las variables que nos sean numeros, es decir, el origen y el destino son valores como "ANL", un valor que dificulta los posteriores calculos. Por eso lo que se hace es convertir en numeros los valores, "ANL" en 1, "DLO" en 2 ... El proceso para hacerlo es el que se muestra a continuación.

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

Tras esto se muestran gráficas determinadas con la libreria antes nombrada "plotly.express" para el analisis de las correlaciones y del caso en particular para ver en detenimiento el origen y destion con la variable de cancelacion.

>Gráficas interactivas de todas las relaciones entre variables(vista general)
![]({{site.baseurl}}/images/grafica_grande.jpg)

>Gráficas de relaciones entre las variables a estudiar
![]({{site.baseurl}}/images/grafica_peque.jpg)

Tras el estudio gráfico procedemos a entrenar nuestro modelo con las variables dictadas y la variable objetivo, dandonos cuenta que no obtenemos ni de cerca un valor valioso para el analisis. Algo que se podia intuir con las gráficas.

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

Visto los resultados del primer modelo se procede a analizar las variables que parecen mas significativas entre ellas graficamente y tras varias pruebas, mostramos aquel modelo que tiene mejores resultados de R_2. Siendo aun asi poco valiosos para determinar que se puede predecir correctamente. Aunque no es bueno que el R_2 este muy ajustado, el resultado no es bueno.

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

    Coeficiente beta1:  [ 0.00148963 -0.00230434]
    Error cuadratico medio: 0.02
    Estadistico R_2: -0.02

{% endhighlight %}

Como conlusión de la realización del modelo de regresión lineal hemos averiguado que este modelo no es suficiente complejo para obtener previsiones concluyentes sobre los datos que se tenian, para esto sería interesante aplicar otros métodos como DeepLearning o KMeans, mucho mas sotisficados.


