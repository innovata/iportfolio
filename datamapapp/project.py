"""임시 방편"""
import sys
PJT_NAME = 'datamap'
sys.path.append(f"/Users/sambong/pjts/{PJT_NAME}")
# 패키지 읽어들이기.
from datamap import models


import pprint
pp = pprint.PrettyPrinter(indent=2)


def find():
    d = models.Data()
    docs = d.find()
    print(f"\n\n docs :\n")
    pp.pprint(docs)
    return docs
