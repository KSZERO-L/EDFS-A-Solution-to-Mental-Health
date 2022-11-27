import requests
import sys
from numpyencoder import NumpyEncoder
import json
from edfs.firebase_cmd import ls

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'

def mkdir(url):

    res = {'Dummy data': ""}
    res = json.dumps(res, cls=NumpyEncoder)
    requests.patch(url, res)

def main(loc):
    
    # loc = sys.argv[1]
    loc = loc + '.json'

    url = NAMENODEURL + loc
    # print(url)
    mkdir(url)

    loc_split = loc.split('/')
    in_dir = '/'.join(loc_split[:-1])
    print("INDIR: ", in_dir)

    return ls.main(in_dir)
