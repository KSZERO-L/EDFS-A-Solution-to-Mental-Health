import pandas as pd
from tqdm import tqdm
import json
import os
import numpy as np
from numpyencoder import NumpyEncoder
import requests
import random

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode/'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode/'

ID = 1

datapath = '../data/'

# partitions
partition_dict = {}
num_partitions = 2

# Load namenode data
for dataname in tqdm(os.listdir(datapath)):
    folderpath = datapath + dataname
    foldername = folderpath.split('/')[-1]
    rng_partition = random.randrange(1,num_partitions+1)
    partition_val = "partition"+str(rng_partition)
    partition_dict[foldername] = partition_val
    for file in os.listdir(folderpath):
        filename = file.split('.')[0]
        final_URL = NAMENODEURL + foldername + '/' + filename + '.json'
        cid = file
        datanode_path = DATANODEURL + partition_val + '/' + foldername + '/' + filename
        TYPE = 'FILE'
        file_obj = {
            'id': ID,
            'type': TYPE,
            'name': file,
            'location': datanode_path
        }
        file_obj = json.dumps(file_obj, cls=NumpyEncoder)
        # print(final_URL)
        # print(file_obj)
        # increase ID global count 
        ID += 1
        requests.put(final_URL, file_obj)

# Load datanode data
for dataname in tqdm(os.listdir(datapath)):
    folderpath = datapath + dataname
    foldername = folderpath.split('/')[-1]
    partition_val = partition_dict[foldername]
    for file in os.listdir(folderpath):
        filepath = folderpath + '/' + file
        filename = file.split('.')[0]
        data = pd.read_csv(filepath)
        data = data.replace(np.nan, 0)
        # data = data[:2]
        columns= data.columns

        # Collecting data
        json_obj = []
        for i in tqdm(range(data.shape[0])):
            cdict = {}
            for j in range(len(columns)):
                cdict[columns[j]] = data.loc[i][columns[j]]

            json_obj.append(cdict)

        final_URL = DATANODEURL + partition_val + '/' + foldername + '/' + filename + '.json'
        print(final_URL)
        # print(json_obj)
        # Load data in the Firebase database
        obj = json.dumps(json_obj, cls=NumpyEncoder)
        requests.put(final_URL, obj)

# data = pd.read_csv('../data/Mental Health in Tech Survey/survey2.csv', index_col=0)
# # data = data[:2]
# columns= data.columns


# # Collecting data
# json_obj = []
# for i in tqdm(range(data.shape[0])):
#     cdict = {}
#     for j in range(len(columns)):
#         cdict[columns[j]] = data.loc[i][columns[j]]

#     json_obj.append(cdict)

# x = [{'Unnamed: 0': 0, 'Age': 37, 'Gender': 'Female', 
# 'Country': 'United States', 'state': 'IL', 'self_employed': '0', 
# 'family_history': 'No', 'treatment': 'Yes', 'work_interfere': 'Often', 
# 'no_employees': '6-25', 'remote_work': 'No', 'tech_company': 'Yes', 'benefits': 'Yes', 
# 'care_options': 'Not sure', 'wellness_program': 'No', 'seek_help': 'Yes', 'anonymity': 'Yes', 
# 'leave': 'Somewhat easy', 'mental_health_consequence': 'No', 'phys_health_consequence': 'No', 
# 'coworkers': 'Some of them', 'supervisor': 'Yes', 'mental_health_interview': 'No', 
# 'phys_health_interview': 'Maybe', 'mental_vs_physical': 'Yes', 'obs_consequence': 'No', 'comments': '0'}
# ]

# final_URL = DATANODEURL + '1' + '/' + 'Mental Health in Tech Survey' + '/' + 'survey2' + '.json'
# print(final_URL)
# print(json_obj)
# # Load data in the Firebase database
# obj = json.dumps(json_obj, cls=NumpyEncoder)
# requests.put(final_URL, obj)


# df = pd.read_csv('../data/Mental Health in Tech Survey/survey2.csv')
# df = df.drop('Unnamed: 0', axis=1)
# df.to_csv("../data/Mental Health in Tech Survey/survey2.csv", index=False)