from typing import Any, Dict, List
from django.views.generic import FormView, ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from rzmr.forms import *
from shop.mixins import DataMixin


class IndexView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/index.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return {**context, **c_def}


class AboutView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/about.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='О заводе')
        return {**context, **c_def}


class QualityView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/quality.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Система качества и сертификации')
        return {**context, **c_def}


class OurCustomerView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/our-customer.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Наши клиенты')
        return {**context, **c_def}


class ForSuppliersView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/for-suppliers.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Поставщикам')
        return {**context, **c_def}


class VacanciesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/vacancies.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Вакансии')
        return {**context, **c_def}


class ContactsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/contacts.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return {**context, **c_def}


class MetalhosesView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/metalhoses.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Металлические рукава')
        return {**context, **c_def}


class FittingsView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/fittings.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Концевая арматура для металлорукавов')
        return {**context, **c_def}


class CorrugationView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ')
        return {**context, **c_def}


class CorrugationStandartnayaView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation_standartnaya.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ средней гибкости')
        return {**context, **c_def}


class CorrugationPovyshennoyGibkostiView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'rzmr/corrugation_povishennoy_gibkosti.html'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title='Гофрированные металлорукава РГМ повышенной гибкости')
        return {**context, **c_def}