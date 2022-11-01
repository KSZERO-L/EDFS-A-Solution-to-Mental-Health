import requests
import sys
from numpyencoder import NumpyEncoder
import json

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'

def mkdir(url):

    res = {}
    res = json.dumps(res, cls=NumpyEncoder)
    requests.patch(url, res)

if __name__ == "__main__":
    
    loc = sys.argv[1]
    loc = loc + '.json'

    url = NAMENODEURL + loc
    # print(url)
    mkdir(url)
