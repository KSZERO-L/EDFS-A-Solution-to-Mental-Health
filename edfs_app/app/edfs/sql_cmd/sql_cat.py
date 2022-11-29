import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import numpy as np
import re

def cat(file_name):
    conn = sqlite3.connect('./test.db')
    cur = conn.cursor()
    a = file_name.split('/')[-1]
    a = a.replace(' ', '_')
    a = a.split('.')[0]
    df = pd.DataFrame()
    for i in range(1,4):
        file = a + '_p' + str(i)
        p = pd.read_sql('''SELECT * FROM '%s' ''' % file, conn)
        df = pd.concat([df,p])
    conn.commit()
    return df