import requests
import sys
from numpyencoder import NumpyEncoder
import json
import pandas as pd
from tqdm import tqdm

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'

def cat(select, url, where, sign, value):

    data = requests.get(url).json()
    print(data)
    # Traversing all the locations of the partitions in the datanode
    fin = []
    for i, key in enumerate(data.keys()):
        location = data[key]['location'] + '.json'
        # print(location)
        records = requests.get(location).json()
        for record in records:
            fin.append(record)
        if i == 0:
            single = fin[0]
            cols = list(single.keys())
            res_df = pd.DataFrame(columns=cols)
        for record in tqdm(records):
            values = record.values()
            res_df.loc[len(res_df)] = values

    # num = len(list(res_df.columns))
    # min_num = min(5, num)
    # res_df = res_df.iloc[:, 0:min_num]

    # print("Head Representation of the DataFrame")
    # print(res_df.head())
    # print("\nShape of the DataFrame")
    # print(res_df.shape)

    res_df.rename(columns=lambda x: x.strip(), inplace=True)
    columns = list(res_df.columns)
    select = select.split(',')
    select = [x.strip() for x in select]
    print(columns)
    print(select)
    print(value, type(value))
    # conditions
    if sign == "=":
        if type(value) == "str":
            res_df = res_df[res_df[where] == value]
        else:
            res_df = res_df[res_df[where] == int(value)]
    elif sign == ">":
        if type(value) == "str":
            res_df = res_df[res_df[where] > value]
        else:
            res_df = res_df[res_df[where] > int(value)]
    elif sign == ">=":
        if type(value) == "str":
            res_df = res_df[res_df[where] >= value]
        else:
            res_df = res_df[res_df[where] >= int(value)]
    elif sign == "<":
        if type(value) == "str":
            res_df = res_df[res_df[where] < value]
        else:
            res_df = res_df[res_df[where] < int(value)]
    elif sign == "<=":
        if type(value) == "str":
            res_df = res_df[res_df[where] <= value]
        else:
            res_df = res_df[res_df[where] <= int(value)]
    elif sign == "!=":
        if type(value) == "str":
            res_df = res_df[res_df[where] != value]
        else:
            res_df = res_df[res_df[where] != int(value)]

    sel_cols = select
    for val in columns:
        if len(sel_cols) == 5:
            break
        if val not in sel_cols:
            sel_cols.append(val)
    
    res_df = res_df.sample(10)
    return res_df[select]


def main(select, from1, where, sign, value):
    
    # loc = sys.argv[1]
    # removing the format of the file
    loc = from1[:-4]

    url = NAMENODEURL + '/' + loc + '.json'
    print(url)
    return cat(select, url, where, sign, value)
