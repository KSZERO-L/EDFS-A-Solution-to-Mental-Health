import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import numpy as np
import re

def readPartition(file, partition):
    conn = sqlite3.connect('./test.db')
    namenode_table = pd.read_sql('''SELECT * from namenode''', conn)
    file = file.replace(' ', '_')
    file = file.split('.')[0]
    partition = str(partition)
    file = file + '_p' + partition
#     print(file)
    print(pd.read_sql('''SELECT * FROM '%s' ''' % file, conn))