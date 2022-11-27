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
        for record in records:
            fin.append(record)
        if i == 0:
            single = fin[0]
            cols = list(single.keys())
            res_df = pd.DataFrame(columns=cols)
        for record in tqdm(records):
            values = record.values()
            res_df.loc[len(res_df)] = values

    num = len(list(res_df.columns))
    min_num = min(5, num)
    res_df = res_df.iloc[:, 0:min_num]

    # print("Head Representation of the DataFrame")
    # print(res_df.head())
    # print("\nShape of the DataFrame")
    # print(res_df.shape)
    return res_df[:5]


def main(loc):
    
    # loc = sys.argv[1]
    # removing the format of the file
    loc = loc[:-4]

    url = NAMENODEURL + loc + '.json'
    return cat(url)
