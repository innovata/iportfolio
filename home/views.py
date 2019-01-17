from django.http import HttpResponse
from django.shortcuts import render

from .models import Project

# Create your views here.

def index(request):
    context = {
        'projects':Project.objects.all()
    }
    return render(request, "home/index.html", context)
