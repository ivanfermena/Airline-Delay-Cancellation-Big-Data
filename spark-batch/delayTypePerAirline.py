from __future__ import division
from pyspark import SparkConf, SparkContext
from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.sql import Row
from datetime import date
import string

conf = SparkConf().setMaster('local[4]').setAppName('airports5')
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

df = sqlContext.read.load("2009-2018.csv", 
                          format='com.databricks.spark.csv', 
                          header='true', 
                          inferSchema='true')

df.registerTempTable("df")

dfA = sqlContext.sql("""
    SELECT OP_CARRIER as Airline, COUNT(CARRIER_DELAY) as Airline_Delay
    FROM df
    WHERE CARRIER_DELAY > 0.0
    GROUP BY OP_CARRIER
""")

dfW = sqlContext.sql("""
    SELECT OP_CARRIER as Airline, COUNT(WEATHER_DELAY) as Weather_delay
    FROM df
    WHERE WEATHER_DELAY > 0.0
    GROUP BY OP_CARRIER
""")

dfN = sqlContext.sql("""
    SELECT OP_CARRIER as Airline, COUNT(NAS_DELAY) as Air_system_delay
    FROM df
    WHERE NAS_DELAY > 0.0
    GROUP BY OP_CARRIER
""")

dfS = sqlContext.sql("""
    SELECT OP_CARRIER as Airline, COUNT(LATE_AIRCRAFT_DELAY) as Security_delay
    FROM df
    WHERE LATE_AIRCRAFT_DELAY > 0.0
    GROUP BY OP_CARRIER
""")

partial1 = dfA.join(dfW,['Airline'],"outer")
partial2 = partial1.join(dfN,['Airline'],"outer")
partial3 = partial2.join(dfS,['Airline'],"outer")


semi_results = partial3.rdd.map(lambda x: (x[0], x[1], x[2], x[3], x[4], x[1] + x[2] + x[3] + x[4]))
results = semi_results.map(lambda x: (x[0], "{:12.2f}".format((x[1]/x[5]) * 100),"{:12.2f}".format((x[2]/x[5]) * 100), "{:12.2f}".format((x[3]/x[5]) * 100), "{:12.2f}".format((x[4]/x[5]) * 100)))

results.toDF(["Airline", "Airline_Delay", "Weather_delay", "Air_system_delay", "Security_delay"]).repartition(1).write.format('com.databricks.spark.csv').option("header", "true").save("delayTypePerAirline")
