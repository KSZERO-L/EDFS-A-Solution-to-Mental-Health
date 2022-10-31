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
num_partitions = 3

# Load namenode data
for dataname in tqdm(os.listdir(datapath)):
    folderpath = datapath + dataname
    foldername = folderpath.split('/')[-1]
    for file in os.listdir(folderpath):
        filename = file.split('.')[0]
        final_URL = NAMENODEURL + foldername + '/' + filename + '.json'
        res = {}
        for i in range(1,num_partitions+1):
            res["p"+str(i)] = {}
        for i in range(1,num_partitions+1):
            datanode_path = DATANODEURL + foldername + '/' + filename + '_p' + str(i)
            TYPE = 'FILE'
            file_obj = {
                'id': ID,
                'type': TYPE,
                'name': file,
                'location': datanode_path
            }
            # increase ID global count 
            ID += 1
            res["p"+str(i)] = file_obj

        res = json.dumps(res, cls=NumpyEncoder)    
        requests.put(final_URL, res)

# Load datanode data
for dataname in tqdm(os.listdir(datapath)):
    folderpath = datapath + dataname
    foldername = folderpath.split('/')[-1]
    for file in os.listdir(folderpath):
        filepath = folderpath + '/' + file
        filename = file.split('.')[0]
        data = pd.read_csv(filepath)
        data = data.replace(np.nan, 0)
        # data = data[:2]
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

            final_URL = DATANODEURL + foldername + '/' + filename + '_p' + str(num) + '.json'
            print(final_URL)
            # print(json_obj)
            # Load data in the Firebase database
            obj = json.dumps(json_obj, cls=NumpyEncoder)
            requests.put(final_URL, obj)

## TEST

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