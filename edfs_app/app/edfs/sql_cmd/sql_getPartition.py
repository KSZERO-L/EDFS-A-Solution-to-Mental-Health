import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import numpy as np
import re

def getPartitionLocations(file):
    namenode_table = pd.read_sql('''SELECT * from namenode''', conn)
    index = 0
    for i in namenode_table['name']:
        if i == file:
            print(namenode_table['location'][index])
    index = index + 1