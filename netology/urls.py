from django.contrib import admin
from django.urls import include, path

from netology.backend import urls as backend_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(backend_urls)),
]
