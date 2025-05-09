from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from shop.mixins import DataMixin
from personal_account.forms import *


class PersonalAccountView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account.html'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('personal-account')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Personal account')
        breadcrumb = [('personal-account', title),]
        c_def = self.get_user_context(title=title, breadcrumb=breadcrumb)
        return {**context, **c_def}


class UserSettingsView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-settings.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Profile settings')
        breadcrumb = [('personal-account', _('Personal account')),]
        c_def = self.get_user_context(title=title,
                                      is_settings=True,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}


class UserOrdersView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-orders.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Orders')
        breadcrumb = [('personal-account', _('Personal account')),]

        orders = self.request.user.get_orders.all()
        paginate_by = 20
        paginator = Paginator(orders, paginate_by)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        c_def = self.get_user_context(title=title,
                                      is_orders=True,
                                      breadcrumb=breadcrumb,
                                      page_obj=page_obj,
                                      orders=orders)

        return {**context, **c_def}


class UserCompaniesView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-companies.html'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        title = _('Organizations')
        breadcrumb = [('personal-account', _('Personal account')),]
        c_def = self.get_user_context(title=title,
                                      is_companies=True,
                                      breadcrumb=breadcrumb)
        return {**context, **c_def}
