import requests
import sys
from numpyencoder import NumpyEncoder
import json
import pandas as pd
import random
from tqdm import tqdm

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'
TYPE = "FILE"

def update_namenode(url, file):
    res = {}
    num_partitions = 3
    for i in range(1,num_partitions+1):
        res["p"+str(i)] = {}
    for i in range(1,num_partitions+1):
        datanode_path = DATANODEURL + url + '_p' + str(i)
        TYPE = 'FILE'
        file_obj = {
            'id': random.randint(100000000000, 999999999999),
            'type': TYPE,
            'name': file,
            'location': datanode_path
        }

        res["p"+str(i)] = file_obj

    res = json.dumps(res, cls=NumpyEncoder)   
    url = NAMENODEURL + '/' + url + '.json' 
    requests.put(url, res)

def update_datanode(url, data, file):

    num_partitions = 3
    columns= data.columns

    data_p1 = data[:len(data)//3]
    data_p2 = data[len(data)//3:len(data)//3*2]
    data_p3 = data[len(data)//3*2:len(data)]
    data_p1.reset_index(drop=True, inplace=True)
    data_p2.reset_index(drop=True, inplace=True)
    data_p3.reset_index(drop=True, inplace=True)
    data_stack = [data_p1, data_p2, data_p3]

    # print(data.shape, data_stack[2].shape)
    
    for num in range(1, num_partitions+1):
        # Collecting data
        json_obj = []
        for i in tqdm(range(data_stack[num-1].shape[0])):
            cdict = {}
            for j in range(len(columns)):
                cdict[columns[j]] = data_stack[num-1].loc[i][columns[j]]

            json_obj.append(cdict)

        final_URL = DATANODEURL + url + '_p' + str(num) + '.json'
        print(final_URL)
        # print(json_obj)
        # Load data in the Firebase database
        obj = json.dumps(json_obj, cls=NumpyEncoder)
        requests.put(final_URL, obj)


def put(url, data, file):

    update_namenode(url, file)
    update_datanode(url, data, file)

if __name__ == "__main__":
    
    loc = sys.argv[1]
    loc = loc[:-4]
    file = loc.split('/')[-1]

    # Test data
    data = pd.DataFrame(columns=["1", "2", "3", "4", "5"])
    data.loc[len(data)] = [1,2,3,4,5]
    data.loc[len(data)] = [1,2,3,4,5]
    data.loc[len(data)] = [1,2,3,4,5]
    data.loc[len(data)] = [1,2,3,4,5]
    data.loc[len(data)] = [1,2,3,4,5]
    data.loc[len(data)] = [1,2,3,4,5]

    # loc = loc + '.json'

    url = NAMENODEURL + loc
    # print(url)
    put(loc, data, file)
