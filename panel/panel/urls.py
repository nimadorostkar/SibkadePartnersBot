from django.contrib import admin
from django.urls import path
from link.views import LinkView
from django.conf.urls.static import static

from panel.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path("links", LinkView.as_view(), name="links"),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)