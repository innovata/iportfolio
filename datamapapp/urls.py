from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bookmark.csv", views.data, name='data'),
    path("world_countries.json", views.data, name='data'),
    path("world_cup_geo.tsv", views.data, name='data'),
]
