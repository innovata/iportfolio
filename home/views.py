from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from .models import Project, Coworker

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
        'project':project,
        'coworkers':project.coworkers.all(),
        'non_coworkers':Coworker.objects.exclude(projects=project).all()
    }
    return render(request, "home/project.html", context)

def join(request, project_id):
    try:
        coworker_id = int(request.POST["coworker"])
        coworker  = Coworker.objects.get(pk=coworker_id)
        project = Project.objects.get(pk=project_id)
    except KeyError:
        return render(request, "home/error.html", {"message":"No selection."})
    except Project.DoesNotExist:
        return render(request, "home/error.html", {"message":"No project."})
    except Coworker.DoesNotExist:
        return render(request, "home/error.html", {"message":"No coworker."})

    coworker.projects.add(project)
    return HttpResponseRedirect(reverse("project", args=(project_id, )))
