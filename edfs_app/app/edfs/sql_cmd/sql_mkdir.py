import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import numpy as np
import re


def mkdir(new_dir):
    a = new_dir.split(' ')
    b = []
    conn = sqlite3.connect('./test.db')
    cur = conn.cursor()
    p = pd.read_sql('''SELECT * from namenode''', conn)
    p = len(p) + 1
    for i in a:
        k = i.split('/')
        b.append(k)
    for i in range(1,len(b[1])-1):
        direct = b[1][0] + '/'
        for j in range(1,i):
            direct = direct + b[1][j] + '/'
        sql = ''' INSERT INTO namenode(id,location,name,type)
                  VALUES(?,?,?,?) '''
        namenode_info = (p,direct,b[1][i],'DIRECTORY')
        cur.execute(sql, namenode_info)
        conn.commit()
        p = p + 1