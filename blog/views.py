from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.permissions import StaffRequiredMixin
from django.urls import reverse_lazy
from django.conf import settings
from blog.models import *
from blog.forms import *
from shop.mixins import DataMixin


class PostListView(DataMixin, ListView):
    model = Post
    template_name = 'blog/post-list.html'
    context_object_name = 'posts'
    paginate_by = 8

    def get_queryset(self) -> QuerySet:
        queryset = Post.objects.filter(
            is_published=True).order_by('-time_create')
        return queryset

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = f'Статьи - {settings.COMPANY_NAME_SHORT}'
        description = f'В данном разделе вы можете ознакомиться со статьями компании {settings.COMPANY_NAME}'
        breadcrumb = [('posts', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PostDetailView(DataMixin, DetailView):
    model = Post
    template_name = 'blog/post-details.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = context['post'].title
        description = context['post'].title
        breadcrumb = [('posts', 'Статьи'),
                      ('', title),]
        c_def = self.get_user_context(title=title,
                                      description=description,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class PostCreateView(StaffRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'blog/post-create.html'
    success_url = reverse_lazy('posts')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Добавление новой статьи'
        breadcrumb = [('posts', 'Статьи'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class PostUpdateView(StaffRequiredMixin, DataMixin, UpdateView):
    model = Post
    form_class = AddPostForm
    template_name = 'blog/post-update.html'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = 'Изменение статьи'
        breadcrumb = [('posts', 'Статьи'),
                      ('', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}
