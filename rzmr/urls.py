from django.urls import path
from rzmr.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('about/quality/', QualityView.as_view(), name='quality'),
    path('about/our-customer/', OurCustomer.as_view(), name='our-customer'),
    path('about/for-suppliers/', ForSuppliers.as_view(), name='for-suppliers'),
    path('about/vacancies/', Vacancies.as_view(), name='vacancies'),
    path('about/contacts/', Contacts.as_view(), name='contacts'),
]
