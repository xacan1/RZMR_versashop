from django.urls import path
from rzmr.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('about/quality/', QualityView.as_view(), name='quality'),
    path('about/our-customer/', OurCustomerView.as_view(), name='our-customer'),
    path('about/for-suppliers/', ForSuppliersView.as_view(), name='for-suppliers'),
    path('about/vacancies/', VacanciesView.as_view(), name='vacancies'),
    path('about/contacts/', ContactsView.as_view(), name='contacts'),
    path('about/metalhoses/', MetalhosesView.as_view(), name='metalhoses'),
    path('about/metalhoses/fittings', FittingsView.as_view(), name='metalhoses-fittings'),
]
