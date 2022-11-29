import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import numpy as np
import re

def rm(file_name):
    conn = sqlite3.connect('./test.db')
    cur = conn.cursor()
    a = file_name.split('/')[-1]
    p = pd.read_sql('''SELECT * from namenode''', conn)
    p = p.drop(p.index[p['name'] == a])
    conn.commit()
    return p