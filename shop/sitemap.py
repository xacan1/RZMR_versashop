from django.contrib.sitemaps import Sitemap
from django.conf import settings
from shop.models import Product


class ProductSitemap(Sitemap):
    changefreq = 'yearly'
    priority = 0.9

    # def get_urls(self, page=..., site=..., protocol=...):
    #     current_domain = site.domain
    #     company_cities = settings.COMPANY_CITIES
    #     print(current_domain)

    #     for subdomain in company_cities:
    #         if subdomain and subdomain in current_domain:
    #             site.domain = f'{subdomain}.{settings.COMPANY_HOST}'
    #             break

    #     return super().get_urls(page, site, protocol)

    def items(self):
        return Product.objects.filter(is_published=True).order_by('time_create')

    def lastmod(self, obj):
        return obj.time_update
