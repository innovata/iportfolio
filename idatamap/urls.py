from django.urls import path

from . import views, resources

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:category>", views.datamap, name="datamap"),
    path("iframe/<int:height>", views.iframe, name="iframe"),
    path("iframe/data/<str:category>", resources.get_data, name='get_data'),
    path("data/<str:category>", resources.get_data, name='get_data'),
    path("images/<str:filename>", resources.get_img, name="get_img"),
    path("assets/js/<str:filename>", resources.get_js, name="get_js"),

    path("elliptic_forces", views.elliptic_forces, name='elliptic_forces'),
]
