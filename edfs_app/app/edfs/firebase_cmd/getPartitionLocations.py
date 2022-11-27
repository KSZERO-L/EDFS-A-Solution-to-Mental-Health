import requests
import sys
from numpyencoder import NumpyEncoder
import json
import pandas as pd
from tqdm import tqdm

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'

def getPartitionLocations(url):

    data = requests.get(url).json()

    # Traversing all the locations of the partitions in the datanode
    locations = []
    for i, key in enumerate(data.keys()):
        location = data[key]['location'] + '.json'
        locations.append(location)

    print("Partition Locations:")
    for loc in locations:
        print(loc)

    return locations

def main(loc):
    
    # loc = sys.argv[1]
    # removing the format of the file
    loc = loc[:-4]

    url = NAMENODEURL + loc + '.json'

    filename = loc.split('/')[-1] + '.csv'
    # print(url)
    res = getPartitionLocations(url)
    return filename, res
