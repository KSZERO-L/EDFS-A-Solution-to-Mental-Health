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

    print("Head Representation of the DataFrame")
    print(res_df.head())
    print("\nShape of the DataFrame")
    print(res_df.shape)
    # print(data)



if __name__ == "__main__":
    
    loc = sys.argv[1]
    num = int(sys.argv[2])
    # removing the format of the file
    loc = loc[:-4]

    url = NAMENODEURL + loc + '.json'
    # print(url)
    readPartition(url, num)
