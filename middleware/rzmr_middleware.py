from django.utils.deprecation import MiddlewareMixin


class SubdomainMiddleware(MiddlewareMixin):
    def _init_(self, get_response):
        self.get_response = get_response

    # def __call__(self, request):
    #     host = request.META.get('HTTP_HOST', '')
    #     response = self.get_response(request)
    #     host = request.META.get('HTTP_HOST', '')
    #     print(host)
    #     return response

    def process_request(self, request):
        host = request.META.get('HTTP_HOST', '')
        print(host)
        request.subdomain = host if len(host) > 1 else None

    # def process_view(request, view_func, view_args, view_kwargs):
    #     pass
