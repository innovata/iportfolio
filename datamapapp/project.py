"""임시 방편"""
import sys
PJT_NAME = 'datamap'
sys.path.append(f"/Users/sambong/pjts/{PJT_NAME}")
# 패키지 읽어들이기.
from datamap import *


import pprint
pp = pprint.PrettyPrinter(indent=2)
import json


def find():
    d = models.Data()
    docs = d.find(projection={'_id':0})
    js = json.dumps(docs)
    print(f"\n\n js :\n")
    pp.pprint(js)
    return docs
