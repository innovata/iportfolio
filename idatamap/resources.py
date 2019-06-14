
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import os
from idatamap import mapdata, APP_PATH
import sys
import inspect

modulename = sys.modules[__name__].__file__


def get_data(request, category):
    print(f"\n{'='*60}\n{modulename} | {inspect.stack()[0][3]}\n category : {category}")
    data = mapdata.get(category=category)
    return HttpResponse(data)

def get_img(request, filename):
    print(f"\n{'='*60}\n{modulename} | {inspect.stack()[0][3]}\n filename : {filename}")
    with open(file=f"{APP_PATH}/templates/idatamap/images/{filename}", mode='rb') as f:
        bin = f.read()
        f.close()
    return HttpResponse(bin)

def get_js(request, filename):
    print(f"\n{'='*60}\n{modulename} | {inspect.stack()[0][3]}\n filename : {filename}")
    with open(file=f"{APP_PATH}/templates/idatamap/assets/js/{filename}", mode='r') as f:
        text = f.read()
        f.close()
    return HttpResponse(text)
