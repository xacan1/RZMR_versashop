from typing import Any
from django.forms import Form
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from shop.mixins import DataMixin
from constructor import request1C


class MetalhoseConstructorView(DataMixin, FormView):
    form_class = Form
    template_name = 'constructor/metalhose-constructor.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Конструктор металлорукава')
        return {**context, **c_def}


# Прокси запросы к 1С
class ProxyRequestView(FormView):
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        # return super().get(request, *args, **kwargs)
        url_request = request.headers.get('Request1C', '')
        request_data = request1C.get_request_to_1C(url_request)
        return HttpResponse(request_data)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
