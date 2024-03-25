from typing import Any
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView
from shop.mixins import DataMixin
from constructor.forms import *
from constructor import request1C


class MetalhoseConstructorView(DataMixin, FormView):
    form_class = ConstructorForm
    template_name = 'constructor/metalhose-constructor.html'

    def get_initial(self) -> dict[str, Any]:
        initial = super().get_initial()
        initial['types_choices'] = request1C.get_types()
        initial['diameters_choices'] = request1C.get_diameters()
        initial['lengths_choices'] = request1C.get_lengths()
        initial['fittings_choices'] = request1C.get_fittings()
        return initial

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Конструктор металлорукава')
        return {**context, **c_def}


# Прокси запросы к серверу 1С
class ProxyRequestView(FormView):
    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        # return super().get(request, *args, **kwargs)
        url_request = request.headers.get('Request1C', '')
        response_data = request1C.get_request_to_1C(url_request)
        return HttpResponse(response_data)

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
