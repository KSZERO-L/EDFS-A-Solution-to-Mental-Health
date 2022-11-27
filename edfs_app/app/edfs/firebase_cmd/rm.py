import requests
import sys
from numpyencoder import NumpyEncoder
import json
import pandas as pd
from tqdm import tqdm
from edfs.firebase_cmd import ls

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

def main(loc):
    
    # loc = sys.argv[1]
    # removing the format of the file
    loc = loc[:-4]

    url = NAMENODEURL + loc + '.json'
    # print(url)
    rm(url)

    loc_split = loc.split('/')
    in_dir = '/'.join(loc_split[:-1])
    print("INDIR: ", in_dir)

    return ls.main(in_dir)
