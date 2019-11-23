from pyspark import SparkContext
import sys
from pyspark.sql import SparkSession
from pyspark.sql.types import *
import pyspark.sql.functions as fn
from pyspark.sql.functions import col
import pandas as pd

# --------- DATA EXTRACTION ---------

# Get SparkSession with SQL in Dataframe and SparkContext
sc = SparkContext()

spark = SparkSession.builder.appName("Aircraft-Delay-Cancelation").getOrCreate()

# Concatena todos los csvs uno detras de otro
#df = spark.read.option("header", "true").csv("../data/2018.csv")

df = pd.read_csv("../data/2018.csv")

print(df.info())

#num_rows = df.count()

#print(num_rows)

# He comprobado con 'df.dropna() y df.fillna(0)' que no hay na en la tabla
# Por tanto los campos que no me interesan son los vacios
#df_cleaned = df.fillna(0).filter(df["DEP_DELAY"] != "").filter(df["DEP_DELAY"] != " ")

print("Numero de NA y null que tienen cada columna:")
print (df.isna().sum())

print("Exemplos de estos valores que no nos interesan:")
##print(df[df['DEP_DELAY'].isna()])

#missing_values = ["n/a", "na", "", " "]from pyspark.sql.functions import col
#df_cleaned = pd.read_csv("../data/2018.csv", na_values = missing_values)

df_cleaned = df[df['DEP_DELAY'].notna()]

print("Revisamos el numero de NA y null que tienen cada columna:")
##print(df_cleaned.isna().sum())

df_airports = spark.createDataFrame(df_cleaned[['ORIGIN','DEST','DEP_DELAY']])

##print(df_airports.dtypes)


# --------- DATA TRANSFORMATION ---------

df_airports = df_airports.withColumn('DEP_DELAY', col("DEP_DELAY").cast(IntegerType()))

df_gb_airports = df_airports.groupby(['ORIGIN', 'DEST'])

df_grouped = df_gb_airports.agg(fn.sum(col('DEP_DELAY')).alias('DEP_DELAY_SUM'))


#df_airports = spark.createDataFrame(df[['ORIGIN','DEST','DEP_DELAY']])

#print(df_airports.dtypes)

#print(df_airports)

#df_group_origin = df_airports.groupBy("ORIGIN")

print(df_grouped.show())

# --------- DATA LOAD ---------

# df.toPandas().to_csv('mycsv.csv')
