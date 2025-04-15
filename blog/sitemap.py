from django.contrib.sitemaps import Sitemap
from blog.models import Post


class PostSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return Post.objects.filter(is_published=True).order_by('time_create')

    def lastmod(self, obj):
        return obj.time_update
