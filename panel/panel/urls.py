from django.contrib import admin
from django.urls import path
from link.views import LinkView, LinkSearchView, LinkItemView
from django.conf.urls.static import static
from panel.settings import STATIC_ROOT, STATIC_URL, MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path("links", LinkView.as_view(), name="links"),
    path("link/<str:code>", LinkItemView.as_view(), name="link"),
    path("link-search", LinkSearchView.as_view(), name="link-search"),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)