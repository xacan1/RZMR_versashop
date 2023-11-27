from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView
from blog.models import *
from shop.mixins import DataMixin


class PostListView(DataMixin, ListView):
    model = Post
    template_name = 'blog/post-list.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self) -> QuerySet[Any]:
        queryset = Post.objects.filter(
            is_published=True).order_by('-time_create')
        return queryset

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Статьи')
        return {**context, **c_def}


class PostDetailView(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post-details.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('posts', 'Статьи'),]
        c_def = self.get_user_context(
            title=context['post'].title, breadcrumb=breadcrumb)
        return {**context, **c_def}
