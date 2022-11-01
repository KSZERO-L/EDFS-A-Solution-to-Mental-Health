import requests
import sys

NAMENODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/namenode'
DATANODEURL = 'https://edfs-dd402-default-rtdb.firebaseio.com/EDFS/datanode'

def ls(url):
    data = requests.get(url).json()
    keys = data.keys()
    res = []
    for key in keys:
        val = data[key].keys()
        if "p1" in val:
            res.append(key+'.csv')
        else:
            res.append(key)
    
    print(res)

if __name__ == "__main__":
    
    loc = sys.argv[1]
    loc = loc + '.json'

    url = NAMENODEURL + loc
    # print(url)
    ls(url)
