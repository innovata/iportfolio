from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Project

# Create your views here.

def index(request):
    context = {
        'projects':Project.objects.all()
    }
    return render(request, "home/index.html", context)

def project(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project dose not exist.")
    context = {
        'project':project
    }
    return render(request, "home/project.html", context)
