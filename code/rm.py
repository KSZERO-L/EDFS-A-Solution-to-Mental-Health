import requests
import sys
from numpyencoder import NumpyEncoder
import json
import pandas as pd
from tqdm import tqdm

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'

def rm(url):

    data = requests.get(url).json()

    # Traversing all the locations of the partitions in the datanode
    locations = []
    for i, key in enumerate(data.keys()):
        location = data[key]['location'] + '.json'
        locations.append(location)

    # delete each partition from datanode
    for loc in locations:
        requests.delete(loc)
    
    # delete the namenode location of the file
    requests.delete(url)

if __name__ == "__main__":
    
    loc = sys.argv[1]
    # removing the format of the file
    loc = loc[:-4]

    url = NAMENODEURL + loc + '.json'
    # print(url)
    rm(url)
