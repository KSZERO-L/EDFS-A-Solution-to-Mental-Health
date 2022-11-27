import requests
import sys
from numpyencoder import NumpyEncoder
import json
import pandas as pd
from tqdm import tqdm

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'

def readPartition(url, num):

    data = requests.get(url).json()

    # Traversing all the locations of the partitions in the datanode
    locations = []
    for i, key in enumerate(data.keys()):
        location = data[key]['location'] + '.json'
        locations.append(location)

    partitions = requests.get(locations[num-1]).json()

    single = partitions[0]
    cols = list(single.keys())
    res_df = pd.DataFrame(columns=cols)

    for record in tqdm(partitions):
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



def main(loc, num):
    
    # loc = sys.argv[1]
    # num = int(sys.argv[2])
    # removing the format of the file
    loc = loc[:-4]

    url = NAMENODEURL + loc + '.json'
    # print(url)
    return readPartition(url, num)
