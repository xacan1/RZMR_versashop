from django.contrib.sitemaps import Sitemap
from shop.models import Product, Category


class CategorySitemap(Sitemap):
    # changefreq = 'yearly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Category.objects.filter(is_published=True).order_by('time_create')

    def lastmod(self, obj):
        return obj.time_update


class ProductSitemap(Sitemap):
    # changefreq = 'yearly'
    priority = 0.9
    protocol = 'https'

    def items(self):
        return Product.objects.filter(is_published=True).order_by('time_create')

    def lastmod(self, obj):
        return obj.time_update
