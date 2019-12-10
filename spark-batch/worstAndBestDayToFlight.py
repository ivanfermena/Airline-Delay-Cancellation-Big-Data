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

dfD = sqlContext.sql("""
    SELECT DAYOFYEAR(FL_DATE) as Day, COUNT(ARR_DELAY) as Delays
    FROM df
    WHERE ARR_DELAY > 0.0
    GROUP BY DAYOFYEAR(FL_DATE)
    ORDER BY DAYOFYEAR(FL_DATE) DESC
""")

dfC = sqlContext.sql("""
    SELECT DAYOFYEAR(FL_DATE) as Day, COUNT(CANCELLED) as Cancelations
    FROM df
    WHERE CANCELLED = 1.0
    GROUP BY DAYOFYEAR(FL_DATE)
    ORDER BY DAYOFYEAR(FL_DATE) DESC
""")

partial1 = dfD.join(dfC,['Day'],"outer")

results = partial1.rdd.map(lambda x: (x[0], x[1], x[2], x[1] + x[2]))
results.toDF(["Day", "Delays", "Cancellations", "Total incidents"]).show()
#results.toDF(["Day", "Delays", "Cancellations", "Total incidents"]).repartition(1).write.format('com.databricks.spark.csv').option("header", "true").save("worstAndBestDayToFlight")
