from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from home import views, APP_PATH


MEDIA_URL = f"{APP_PATH}/templates/home"
MEDIA_ROOT = f"{APP_PATH}/templates/home"

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^datamap$|^istock$", views.redirect_to_app, name="redirect_to_app"),
    path("<str:filename>", views.get_ico, name="get_ico"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""

"""
