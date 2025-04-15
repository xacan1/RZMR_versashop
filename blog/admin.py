from django.contrib import admin
from blog.models import *


class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ('title', 'photo', 'time_create',
                    'time_update', 'is_published',)
    list_display_links = ('title',)
    list_filter = ('time_create', 'is_published',)
    search_fields = ('title',)
    list_editable = ('is_published',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)
