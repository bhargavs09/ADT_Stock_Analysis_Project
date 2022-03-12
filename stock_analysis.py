from pyspark.sql import SparkSession;
spark = SparkSession.builder.master("local").appName("stocks").getOrCreate()

from pyspark.sql import SQLContext
from pyspark.sql.functions import col,lag
import pyspark.sql.functions as f
from pyspark.sql import Window
import yfinance as fi

import pandas as pd
import plotly.express as px  # (version 4.7.0 or higher)
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output  # pip install dash (version 2.0.0 or higher)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(__name__, external_stylesheets=external_stylesheets)


s1 = input("Enter the first stock:")

s2 = input("Enter the second stock:")

fi_data1 = fi.download(s1,'2001-01-01','2021-02-01')

fi_data2 = fi.download(s2,'2001-01-01','2021-02-01')


raw_df_1 = spark.createDataFrame(data=fi_data1)
raw_df_1.printSchema();
raw_df_1.show()
raw_df_2 = spark.createDataFrame(data=fi_data2)
raw_df_2.printSchema();
raw_df_2.show()
raw_df_1.createOrReplaceTempView("stock1")
raw_df_2.createOrReplaceTempView("stock2")

df_1 = spark.sql(" select 'stock1' ,`Adj Close` as adjclose, ROW_NUMBER() OVER(order by 0) as row_num from stock1")
df_1.show()

w1 = Window.partitionBy('stock1').orderBy('row_num')
returns_df_1 = df_1.withColumn('prev_close',f.lag(col('adjclose')).over(w1))
returns_df_1.show()

returns_df_1.createOrReplaceTempView("stock11")
returns_df_1 = spark.sql("select row_num,stock1,adjclose,prev_close, ((adjclose)-(prev_close)) / (prev_close) as returns from stock11 ")
returns_df_1.show()

stock1_mean = returns_df_1.agg({'returns' : 'mean'})
stock1_variance = returns_df_1.agg({'returns' : 'variance'})
stock1_std_dev = returns_df_1.agg({'returns' : 'stddev'})

stock1_mean.show()
stock1_variance.show()
stock1_std_dev.show()

df_2 = spark.sql("select 'stock2',`Adj Close` as adjclose, ROW_NUMBER() OVER(order by 0) as row_num2 from stock2")
w2 = Window.partitionBy('stock2').orderBy('row_num2')
returns_df_2 = df_2.withColumn('prev_close',f.lag(col('adjclose')).over(w2))
returns_df_2.createOrReplaceTempView("stock21")
returns_df_2 = spark.sql("select row_num2,stock2,adjclose,prev_close, ((adjclose)-(prev_close)) / (prev_close) as returns from stock21 ")

stock2_mean = returns_df_2.agg({'returns' : 'mean'})
stock2_variance = returns_df_2.agg({'returns' : 'variance'})
stock2_std_dev = returns_df_2.agg({'returns' : 'stddev'})

stock2_mean.show()
stock2_variance.show()
stock2_std_dev.show()

spark.stop()
