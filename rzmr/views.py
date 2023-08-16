from django.views.generic import FormView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rzmr.forms import *
from shop.mixins import DataMixin

class IndexView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Российский завод металлорукавов')
        return {**context, **c_def}
