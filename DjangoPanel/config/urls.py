from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from . import views
from rest_framework import permissions

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
]

