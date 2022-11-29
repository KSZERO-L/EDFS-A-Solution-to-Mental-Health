import pandas as pd
import sqlite3
from sqlite3 import Error
import os
import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt
import plotly.express as px



conn = sqlite3.connect('./test.db')

def sql_input1(a,b,c,d,e):
    return pd.read_sql('''SELECT %s from %s where %s %s %s''' %(a,b,c,d,e), conn)

def sql_input2(a,b,c,d,e,f,g,h,i,j,k,l):
    return pd.read_sql('''SELECT %s from %s where %s %s %s group by %s having %s %s %s order by %s %s limit %s''' %(a,b,c,d,e,f,g,h,i,j,k,l), conn)

def sql_count():
    p1 = pd.read_sql('''SELECT mental_health_consequence, count(*) from Survey_p1 group by mental_health_consequence''', conn)
    p2 = pd.read_sql('''SELECT mental_health_consequence, count(*) from Survey_p2 group by mental_health_consequence''', conn)
    p3 = pd.read_sql('''SELECT mental_health_consequence, count(*) from Survey_p3 group by mental_health_consequence''', conn)
    result = pd.DataFrame(columns=['mental_health_consequence','count(*)'])
    result_list1 = []
    result_list2 = []
    for i in range(len(p1)):
        for j in range(len(p2)):
            for k in range(len(p3)):
                if p1.iloc[i][0] == p2.iloc[j][0] == p3.iloc[k][0]:
                    result_list1.append(p1.iloc[i][0])
                    result_list2.append(p1.iloc[i][1] + p2.iloc[i][1] + p3.iloc[i][1])
    result['mental_health_consequence'] = result_list1
    result['count(*)'] = result_list2
    f = plt.figure()
    f.set_figwidth(20)
    f.set_figheight(15)
    plt.bar(result['mental_health_consequence'], result['count(*)'])
    plt.xticks(rotation=90)


def sql_sum():
    p1 = pd.read_sql('''SELECT Continent, sum(`Population (historical estimates)`) from `prevalence-of-depression-males-vs-females_p1` group by Continent having Year = max(Year)''', conn)
    p2 = pd.read_sql('''SELECT Continent, sum(`Population (historical estimates)`) from `prevalence-of-depression-males-vs-females_p2` group by Continent having Year = max(Year)''', conn)
    p3 = pd.read_sql('''SELECT Continent, sum(`Population (historical estimates)`) from `prevalence-of-depression-males-vs-females_p3` group by Continent having Year = max(Year)''', conn)
    result = pd.DataFrame(columns=['Continent','sum(`Population (historical estimates)`)'])
    result_list1 = []
    result_list2 = []
    for i in range(len(p1)):
        for j in range(len(p2)):
            for k in range(len(p3)):
                if p1.iloc[i][0] == p2.iloc[j][0] == p3.iloc[k][0]:
                    result_list1.append(p1.iloc[i][0])
                    if i < len(p3):
                        result_list2.append((p1.iloc[i][1] + p2.iloc[i][1] + p3.iloc[i][1]))
                    else:
                        result_list2.append((p1.iloc[i][1] + p2.iloc[i][1]))
    result['Continent'] = result_list1
    result['sum(`Population (historical estimates)`)'] = result_list2
    fig = px.bar(result, x="Continent", y="sum(`Population (historical estimates)`)", barmode="group")
    fig.show()
    return result