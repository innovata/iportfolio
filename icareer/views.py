from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse

# from .models import Project, Coworker
from home import APP_PATH
import os
import re
import sys
import inspect

# Create your views here.


def index(request):
    # return HttpResponse('Career-Project')
    return render(request, "icareer/bootstrap3.4/index.html")
