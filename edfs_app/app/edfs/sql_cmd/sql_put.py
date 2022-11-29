import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import numpy as np
import re

def put(file, location, partition):
    conn = sqlite3.connect('./test.db')
    cur = conn.cursor()
    casedf = pd.read_csv(file)
    #equal length partition
    casedf_p1 = casedf[:len(casedf)//3]
    casedf_p2 = casedf[len(casedf)//3:len(casedf)//3*2]
    casedf_p3 = casedf[len(casedf)//3*2:len(casedf)]
    
    file_name = file.split('\\')[-1]
    file_name = file_name.split('.')[0]
    file_name = file_name.replace(' ','_')
    file_name_p1 = file_name + '_p1'
    file_name_p2 = file_name + '_p2'
    file_name_p3 = file_name + '_p3'
    
#     casedf_p1.to_csv(file_name_p1 + '.csv')
#     casedf_p2.to_csv(file_name_p2 + '.csv')
#     casedf_p3.to_csv(file_name_p3 + '.csv')
    
    casedf_p1.to_sql(file_name_p1, conn, if_exists='append', index = False)
    cur.close()
    casedf_p2.to_sql(file_name_p2, conn, if_exists='append', index = False)
    cur.close()
    casedf_p3.to_sql(file_name_p3, conn, if_exists='append', index = False)
    cur.close()
    
    conn = sqlite3.connect('./test.db')
    cur = conn.cursor()
    p = pd.read_sql('''SELECT * from namenode''', conn)
    p = len(p) + 1
    sql = ''' INSERT INTO namenode(id,location,name,type) VALUES(?,?,?,?) '''
    namenode_info = (p,location,file,'FILE')
    cur.execute(sql, namenode_info)
    conn.commit()
    cur.close()
    p = pd.read_sql('''SELECT * from namenode''', conn)
    return p