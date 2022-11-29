import requests
import sys
from numpyencoder import NumpyEncoder
import json
import pandas as pd
from tqdm import tqdm

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'

def cat(url):

    data = requests.get(url).json()
    print(data)
    # Traversing all the locations of the partitions in the datanode
    fin = []
    for i, key in enumerate(data.keys()):
        location = data[key]['location'] + '.json'
        # print(location)
        records = requests.get(location).json()
        records = records
        for record in records:
            fin.append(record)
        if i == 0:
            single = fin[0]
            cols = list(single.keys())
            res_df = pd.DataFrame(columns=cols)
        if i == 1:
            single = fin[0]
            cols = list(single.keys())
            res_df1 = pd.DataFrame(columns=cols)
        if i == 2:
            single = fin[0]
            cols = list(single.keys())
            res_df2 = pd.DataFrame(columns=cols)

        for record in tqdm(records):
            values = record.values()
            if i == 0:
                res_df.loc[len(res_df)] = values
            if i == 1:
                res_df1.loc[len(res_df1)] = values
            if i == 2:
                res_df2.loc[len(res_df2)] = values

    # num = len(list(res_df.columns))
    # min_num = min(5, num)
    # res_df = res_df.iloc[:, 0:min_num]

    # print("Head Representation of the DataFrame")
    # print(res_df.head())
    # print("\nShape of the DataFrame")
    # print(res_df.shape)
    return res_df, res_df1, res_df2


def main(loc):
    
    # loc = sys.argv[1]
    # removing the format of the file
    loc = loc[:-4]

    url = NAMENODEURL + loc + '.json'
    print(url)
    return cat(url)
