from django.http import Http404
from django.template import TemplateDoesNotExist


class TemplateNotFoundMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, TemplateDoesNotExist):
            raise Http404(f'Template not found: {exception}')
        return None
