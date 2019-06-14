
from tests import *


def print_cursor_explain(cursor):
    """https://api.mongodb.com/python/current/api/pymongo/cursor.html"""
    cursor.explain()

def print_obj(object):
    #print(f"\n\n objectname : {object.__name__}")
    print(f"\n\n dir(object) :\n\n {dir(object)}")
    #print(f"\n\n object.__dir__() :\n\n {object.__dir__()}")

    print(f"\n\n object.__dict__ :\n")
    pp.pprint(object.__dict__)

    # __class__
    print(f"\n\n object.__class__ : {object.__class__}")
    print(f"\n\n object.__class__.__dict__ :\n")
    pp.pprint(object.__class__.__dict__)
    print(f"\n\n object.__class__.__name__ : {object.__class__.__name__}")
    print(f"\n\n object.__class__.__module__ : {object.__class__.__module__}")

    #print(f"\n\n object.objects : {object.objects}")

def print_frame(frame):
    # args
    print(f"\n\n inspect.getargvalues(frame).locals :\n")
    pp.pprint(inspect.getargvalues(frame).locals)

def print_df(df):
    print(f"\n df :\n\n{df}\n")
    print(f"\n df.info() :\n")
    pp.pprint(df.info())

def print_dics(dics):
    print(f"\n dic(s) :\n")
    pp.pprint(dics)

def print_docs(obj):
    print(f"\n obj.docs :\n")
    pp.pprint(obj.docs)

    print(f"\n obj.docs.brief :")
    print(f"\n len(obj.docs): {len(obj.docs)}")
    df = obj.get_df()
    print(f"\n obj.docs.cols : {df.columns}\n")

#============================================================
# datamap 에만 적용.
#============================================================

def print_req(request):
    print(f"\n request : {request}\n")
    print(f"\n dir(request) : {dir(request)}\n")
    print(f"\n request.__dict__ :\n")
    pp.pprint(request.__dict__)
    print(f"\n request.path : {request.path}\n")
    print(f"\n request.path_info : {request.path_info}\n")

def debug_openfiletext(f):
    print(f"\n f.read() :\n\n{f.read()}\n")
