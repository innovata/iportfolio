from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

# from .models import Project, Coworker
from home import APP_PATH
import os
import re
import sys
import inspect
# modulename = sys.modules[__name__].__file__

# Create your views here.

#============================================================
# HTML Provider.
#============================================================

def index(request):
    # return render(request, "home/html5up/solidstate.html")
    # return render(request, "home/bootstrap4/index.html")
    return render(request, "home/bootstrap3.4/index.html")

def redirect_to_app(request):
    print(f"{'#'*60}\nWARNING: APP-URL로 가고 싶으면, APP-name 뒤에 '/'를 반드시 붙여라 임마. ")
    return HttpResponseRedirect(f"{request.path}/")


#============================================================
# Resource Provider.
#============================================================

def get_ico(request, filename):
    with open(file=f"{APP_PATH}/static/home/images/favicon/{filename}", mode='rb') as f:
        bin = f.read()
        f.close()
    return HttpResponse(bin)



#============================================================
# 배움용 코드 -->  다른 APP으로 만들던가 지우던가 해라.
#============================================================

'''.

def index1(request):
    """프로젝트 리스트 연습"""
    context = {
        'project':project,
        'coworkers':project.coworkers.all(),
        'non_coworkers':Coworker.objects.exclude(projects=project).all()
    }
    return render(request, "home/projects.html", context)

def projects(request, project_id):
    try:
        project = Project.objects.get(pk=project_id)
    except Project.DoesNotExist:
        raise Http404("Project dose not exist.")
    else:
        context = {
            'project':project,
            'coworkers':project.coworkers.all(),
            'non_coworkers':Coworker.objects.exclude(projects=project).all()
        }
        return render(request, "home/projects.html", context)

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
    return HttpResponseRedirect(reverse("projects", args=(project_id, )))

'''
