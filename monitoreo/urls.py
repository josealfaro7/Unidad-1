from django.contrib import admin
from django.urls import path
from dispositivos.views import panel

urlpatterns = [
    path("admin/", admin.site.urls),
    path("panel/", panel),
]
