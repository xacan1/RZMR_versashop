from django.urls import path
from blog.views import *

urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/<slug:post_slug>/', PostDetailView.as_view(), name='post'),
    path('create-post/', PostCreateView.as_view(), name='create-post'),
    path('update-post/<slug:post_slug>/', PostUpdateView.as_view(), name='update-post'),
]
