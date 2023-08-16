from django.urls import path
from rzmr.views import *

urlpatterns = [
    path('', IndexView.as_view(), name='home')
]
