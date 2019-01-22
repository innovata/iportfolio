from django.http import HttpResponse
from django.shortcuts import render

from . import project
import pprint
pp = pprint.PrettyPrinter(indent=2)
import os
APP_ROOT_PATH = '/datamap'
APP_DATA_PATH = 'datamapapp/data/'

# Create your views here.

def index(request):
    debug_object(request)
    #return HttpResponse("This is datamap app.")
    #return HttpResponse(project.find())
    return render(request, "datamapapp/index.html")


def data(request):
    #debug_object(request)
    #filename = request.path.replace('/datamap/', '')
    head, tail = os.path.split(request.path)
    print(f"\n filename : {tail}\n")
    f = open(file=f"datamapapp/data/{tail}", mode='r')
    print(f"\n f : {f}\n")
    text = f.read()
    f.close()
    return HttpResponse(text)


def debug_object(request):
    print(f"\n request : {request}\n")
    print(f"\n dir(request) : {dir(request)}\n")
    print(f"\n request.__dict__ :\n")
    pp.pprint(request.__dict__)
    print(f"\n request.path : {request.path}\n")
    print(f"\n request.path_info : {request.path_info}\n")

def debug_openfiletext(f):
    print(f"\n f.read() :\n\n{f.read()}\n")
