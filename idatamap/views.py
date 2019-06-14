
from idatamap import *

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
#https://docs.djangoproject.com/en/2.2/topics/http/shortcuts/
from idatamap import APP_PATH
import sys
import inspect
import pprint
pp = pprint.PrettyPrinter(indent=2)
modulename = sys.modules[__name__].__file__
# import json
# from io import StringIO


# Create your views here.


def index(request):
    print(f"\n{'='*60}\n{modulename} | {inspect.stack()[0][3]}")
    print(" request.__dict__ :")
    # pp.pprint(request.__dict__)
    # return HttpResponse(str(request.__dict__))
    return HttpResponseRedirect(f"{request.path}Tech")

def datamap(request, category):
    return render(request, "idatamap/datamap.html", context={'category':category})

def iframe(request, height):
    return render(request, "idatamap/shortcut.html", context={'category':'Tech','frame_h':height})

def elliptic_forces(request):
    return render(request, "idatamap/elliptic_forces.html")
