from django.urls import path, re_path
from blog.views import PostList, PostItem

urlpatterns = [
    path("posts", PostList.as_view(), name="posts"),
    path('post-item/<int:id>', PostItem.as_view(), name='post-item'),
]