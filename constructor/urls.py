from django.urls import path
from constructor.views import *


urlpatterns = [
    path('metalhose-constructor/', MetalhoseConstructorView.as_view(), name='metalhose-constructor'),
    path('constructor_api/v1/proxy_get_request/', ProxyRequestView.as_view()),
]
