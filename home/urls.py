from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:project_id>", views.projects, name="projects"),
    path("<int:project_id>/join", views.join, name="join"),
]
