from pyspark import SparkContext
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as fn
from pyspark.sql.functions import col

#
# TODO: Estudio de retrasos de los vuelos por origen y destino
#
# Uso pandas para mayor facilidad a la hora de tratar la extraccion y tratamiento
# de los datos

import pandas as pd

# --------- DATA EXTRACTION ---------

# Get SparkSession with SQL in Dataframe and SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("Aircraft-Delay-Cancelation").getOrCreate()

# Concatena todos los csvs uno detras de otro
# df = pd.read_csv("../data/*.csv")
df = pd.read_csv("../data/2018.csv")

print(df.info())

num_rows = df.count()

print("Numero de lineas extraidas en el dataset:")
print(num_rows)

print("Numero de NA y null que tienen cada columna:")
print (df.isna().sum())

print("Exemplos de estos valores que no nos interesan:")
print(df[df['DEP_DELAY'].isna()])

#missing_values = ["n/a", "na", "", " "]from pyspark.sql.functions import col
#df_cleaned = pd.read_csv("../data/2018.csv", na_values = missing_values)

df_cleaned = df[df['DEP_DELAY'].notna()]

print("Revisamos el numero de NA y null que tienen cada columna:")
print(df_cleaned.isna().sum())

df_airports = spark.createDataFrame(df_cleaned[['ORIGIN','DEST','DEP_DELAY']])

# Comprobamos los tipos de las columnas para no tener error de typos en el sum
print(df_airports.dtypes)

# --------- DATA TRANSFORMATION ---------

# Cogemos las columnas que nos interesan y las casteamos a Integer
df_airports = df_airports.withColumn('DEP_DELAY', col("DEP_DELAY").cast(IntegerType()))

# Agrupamos por Origen y destino
df_gb_airports = df_airports.groupby(['ORIGIN', 'DEST'])

# Hacemos la suma por del retraso a partir del grupo
df_grouped = df_gb_airports.agg(fn.sum(col('DEP_DELAY')).alias('DEP_DELAY_SUM'))

df_grouped = df_grouped.sort(fn.desc("DEP_DELAY_SUM"))

print(df_grouped.show())

df_grouped_pandas = df_grouped.toPandas()

# --------- DATA LOAD ---------

df_grouped_pandas.to_csv('../data/load.csv')
