"""
Title: pyspark at pycharm
Author: Joon Lim
Date: 2015.02.14

Prerequisite:
    1. py4j ('sudo easy_install py4j' in case you don't have)
    2. pyspark folder needs to be placed under the project folder and be selected as a source root.
"""
import numpy as np
import custom_env
custom_env.set_env()

from pyspark import SparkContext, SparkConf


sc = SparkContext('local')

# broadcasting example
broadcastVar = sc.broadcast([1, 2, 3])
print broadcastVar.value

# accumulator example
accum = sc.accumulator(0)
sc.parallelize([1, 2, 3, 4]).foreach(lambda x: accum.add(x))
print accum.value

# Initialize SparkContext
rdd = sc.parallelize(map(lambda x: x[0] + x[1], np.random.randn(100, 2)))
print (rdd.mean(), rdd.stdev())

