"""versa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from main.views import PageNotFound
from blog.sitemap import PostSitemap
from shop.sitemap import CategorySitemap, ProductSitemap
from rzmr.sitemap import RzmrSitemap


urlpatterns = []
sitemaps = {
    'posts': PostSitemap,
    'category': CategorySitemap,
    'products': ProductSitemap,
    'rzmr': RzmrSitemap,
}

rzmr_patterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('main.urls')),
    path(f'{settings.ADMIN_PANEL_URL}/', admin.site.urls, name='admin-panel'),
    path('', include('rzmr.urls')),
    path('', include('api.urls')),
    path('shop/', include('shop.urls')),
    path('', include('personal_account.urls')),
    path('', include('blog.urls')),
    path('', include('constructor.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
]

urlpatterns += i18n_patterns(*rzmr_patterns, prefix_default_language=False)

if settings.DEBUG:
    # import debug_toolbar
    # urlpatterns += path('__debug__/', include('debug_toolbar.urls')),
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = PageNotFound.as_view()
admin.site.site_header = 'Панель администрирования VERSA'
admin.site.site_title = 'Панель администрирования VERSA'
admin.site.index_title = settings.COMPANY_NAME
