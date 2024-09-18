from django.contrib import admin
from django.urls import path
from link.views import LinkView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("links", LinkView.as_view(), name="links"),
]
