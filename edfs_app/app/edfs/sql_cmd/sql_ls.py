import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import numpy as np
import re

def ls(dir_search):
    conn = sqlite3.connect('./test.db')
    cur = conn.cursor()
    p = pd.read_sql('''SELECT * from namenode''', conn)
    a = dir_search.split('/')[2:]
    direct = "./"
    for i in a:
        direct = direct + i
    d = p[p["location"] == direct]
    ans = []
    for i in d['name']:
        ans.append(i)
    conn.commit()
    return ans
