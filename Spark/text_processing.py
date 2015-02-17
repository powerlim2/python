"""
Title: Text processing with pyspark at pycharm
Author: Joon Lim
Date: 2015.02.14

Prerequisite (default - pip install):
    1. py4j (easy_install py4j)
    2. pyspark folder needs to be placed under the project folder and be selected as a source root.
    3. cython (v > 0.11)
    4. sphinx (v >=0.6.1) - documentation package
    5. cypari (easy_install -U)
    4. snappy (v >= 2.2) - high performance network analysis package (http://www.math.uic.edu/t3m/SnapPy/installing.html)
        4.1 snappy is a bit tricky to install: need to do "brew install snappy" first
        4.2 sudo pip install python-snappy
        4.3 set up hadoop-snappy
"""
import custom_env
custom_env.set_env()

from pyspark import SparkContext, SparkConf


sc = SparkContext('local')
logData = sc.textFile("REAME.md").cache()

numAs = logData.filter(lambda s: 'a' in s).count()
numBs = logData.filter(lambda s: 'b' in s).count()

print "Lines with a: %i, lines with b: %i" % (numAs, numBs)
