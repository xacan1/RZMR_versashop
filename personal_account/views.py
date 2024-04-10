from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from shop.mixins import DataMixin
from personal_account.forms import *


class PersonalAccountView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Личный кабинет')
        return {**context, **c_def}


class UserSettingsView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-settings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', 'Личный кабинет'),]
        c_def = self.get_user_context(
            title='Настройки пользователя', is_settings=True, breadcrumb=breadcrumb)
        return {**context, **c_def}


class UserOrdersView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-orders.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', 'Личный кабинет'),]
        c_def = self.get_user_context(
            title='Заказы', is_orders=True, breadcrumb=breadcrumb)
        return {**context, **c_def}


class UserCompaniesView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-companies.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', 'Личный кабинет'),]
        c_def = self.get_user_context(
            title='Организации', is_companies=True, breadcrumb=breadcrumb)
        return {**context, **c_def}
