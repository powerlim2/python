"""
Title: pyspark at pycharm
Author: Joon Lim
Date: 2015.02.14

Prerequisite:
    1. py4j ('sudo easy_install py4j' in case you don't have)
    2. pyspark folder needs to be placed under the project folder and be selected as a source root.
"""
import os
import sys
import numpy as np


# Path for spark source folder
os.environ['SPARK_HOME'] = "/Users/joonhyunglim/spark-1.2.1-bin-hadoop1"
# Append pyspark to Python Path
sys.path.append("/Users/joonhyunglim/spark-1.2.1-bin-hadoop1/python")

# importing pyspark lib should come after setting up the spark path
try:
    from pyspark import SparkContext, SparkConf

except ImportError as e:
    print ("Can not import Spark Modules", e)
    sys.exit(1)


# Initialize SparkContext
sc = SparkContext('local')
rdd = sc.parallelize(map(lambda x: x[0] + x[1], np.random.randn(100, 2)))
print (rdd.mean(), rdd.stdev())

