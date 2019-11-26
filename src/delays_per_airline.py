from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as fn
import pandas as pd

# Get SparkSession with SQL in Dataframe and SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("Aircraft-Delay-Cancelation").getOrCreate()

df = pd.read_csv("../data/2018.csv")

num_rows = df.count()

print("Numero de lineas extraidas en el dataset:")
print(num_rows)

print("Numero de NA y null que tienen cada columna:")
print(df.isna().sum())

df_cleaned = df[df['DEP_DELAY'].notna()]
df_airports = spark.createDataFrame(df_cleaned[['ORIGIN', 'DEST', 'DEP_DELAY']])

df_airlines = df_airports.groupBy()