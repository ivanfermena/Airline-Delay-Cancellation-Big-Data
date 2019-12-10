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
    SELECT MONTH(FL_DATE) as Month, COUNT(ARR_DELAY) as Delays
    FROM df
    WHERE ARR_DELAY > 0.0
    GROUP BY MONTH(FL_DATE)
    ORDER BY MONTH(FL_DATE) DESC
""")

dfC = sqlContext.sql("""
    SELECT MONTH(FL_DATE) as Month, COUNT(CANCELLED) as Cancelations
    FROM df
    WHERE CANCELLED = 1.0
    GROUP BY MONTH(FL_DATE)
    ORDER BY MONTH(FL_DATE) DESC
""")

partial1 = dfD.join(dfC,['Month'],"outer")

results = partial1.rdd.map(lambda x: (x[0], x[1], x[2], x[1] + x[2]))
results.toDF(["Month", "Delays", "Cancellations", "Total incidents"]).show()
#results.toDF(["Month", "Delays", "Cancellations", "Total incidents"]).repartition(1).write.format('com.databricks.spark.csv').option("header", "true").save("worstAndBestMonthToFlight")
