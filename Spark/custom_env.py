"""
Title: Custom Environment for PySpark with Pycharm
Author: Joon Lim
Date: 2015.02.14

Prerequisite:
    1. py4j ('sudo easy_install py4j' in case you don't have)
    2. pyspark folder needs to be placed under the project folder and be selected as a source root.
    3. cython (v > 0.11)
    4. sphinx (v >=0.6.1) - documentation package
    4. snappy (v >= 2.2) - high performance network analysis package
"""
import os
import sys


def set_env():
    """
    this is to set up spark environment within pycharm
    """
    # Path for spark source folder
    os.environ['SPARK_HOME'] = "/Users/joonhyunglim/spark-1.2.1-bin-hadoop1"
    # Append pyspark to Python Path
    sys.path.append("/Users/joonhyunglim/spark-1.2.1-bin-hadoop1/python")




