from django.http import HttpResponse
from django.shortcuts import render

from . import project
# Create your views here.


def index(request):
    #return HttpResponse("This is datamap app.")
    return HttpResponse(project.find())
