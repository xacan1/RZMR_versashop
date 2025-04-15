from django.contrib.sitemaps import Sitemap
from shop.models import Product


class ProductSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.9

    def items(self):
        return Product.objects.filter(is_published=True).order_by('time_create')

    def lastmod(self, obj):
        return obj.time_update
