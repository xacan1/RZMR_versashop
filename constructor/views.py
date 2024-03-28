from typing import Any
import io
from django.http import HttpRequest, HttpResponse, FileResponse
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
    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.buffer = io.BytesIO()
    
    def __del__(self) -> None:
        self.buffer.close()

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        # return super().get(request, *args, **kwargs)
        url_request = request.headers.get('Request1C', '')
        response_data = request1C.get_request_to_1C(url_request)

        if type(response_data) is str:
            response = HttpResponse(response_data)
        else:
            self.buffer.write(response_data)
            self.buffer.seek(0)
            response = FileResponse(self.buffer, as_attachment=False, filename='example.png')
            # print(len(self.buffer.getvalue()))

        return response

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
