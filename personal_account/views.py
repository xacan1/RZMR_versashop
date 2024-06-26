from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.utils.translation import gettext_lazy as _
from shop.mixins import DataMixin
from personal_account.forms import *


class PersonalAccountView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Personal account'))
        return {**context, **c_def}


class UserSettingsView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-settings.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),]
        c_def = self.get_user_context(
            title=_('Profile settings'), is_settings=True, breadcrumb=breadcrumb)
        return {**context, **c_def}


class UserOrdersView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-orders.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),]

        orders = self.request.user.get_orders.all()
        paginate_by = 20
        paginator = Paginator(orders, paginate_by)
        page_number = self.request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        c_def = self.get_user_context(title=_('Orders'),
                                      is_orders=True,
                                      breadcrumb=breadcrumb,
                                      page_obj=page_obj,
                                      orders=orders)

        return {**context, **c_def}


class UserCompaniesView(LoginRequiredMixin, DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'personal_account/personal-account-companies.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),]
        c_def = self.get_user_context(
            title=_('Organizations'), is_companies=True, breadcrumb=breadcrumb)
        return {**context, **c_def}
