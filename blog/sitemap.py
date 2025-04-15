from django.contrib.sitemaps import Sitemap
from .models import Post


class PostSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.5

    def items(self):
        return Post.objects.filter(is_published=True)
    
    def lastmod(self, obj):
        return obj.time_update

