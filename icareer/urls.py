from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from icareer import views, APP_PATH


urlpatterns = [
    path("", views.index, name="index"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
