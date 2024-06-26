from django.views.generic import FormView, CreateView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from main.models import *
from main.forms import *
from shop.mixins import DataMixin


class PageNotFound(FormView):
    form_class = SimpleForm
    template_name = 'main/page404.html'

    def get(self, request, *args, **kwargs):
        response = super().get(request, *args, **kwargs)
        response.status_code = 404
        return response


class LoginUserView(DataMixin, auth_views.LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


class LogoutUserView(auth_views.LogoutView):
    next_page = 'home'


class RegisterUserView(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('registration-success')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=_('Register'))
        return {**context, **c_def}


class RegisterUserSuccessView(DataMixin, FormView):
    form_class = SimpleForm
    template_name = 'main/registration-success.html'


class VersaPasswordChangeView(DataMixin, auth_views.PasswordChangeView):
    form_class = VersaPasswordChangeForm
    template_name = 'main/password-change.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),
                      ('user-settings', _('Profile settings')),]
        c_def = self.get_user_context(
            title='Изменение пароля', breadcrumb=breadcrumb)
        return {**context, **c_def}


class VersaPasswordChangeDoneView(DataMixin, auth_views.PasswordChangeDoneView):
    template_name = 'main/password-change-done.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),
                      ('user-settings', _('Profile settings')),]
        c_def = self.get_user_context(
            title='Пароль успешно изменен!', breadcrumb=breadcrumb)
        return {**context, **c_def}


class VersaPasswordResetView(DataMixin, auth_views.PasswordResetView):
    form_class = VersaPasswordResetForm
    template_name = 'main/password-reset.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),
                      ('user-settings', _('Profile settings')),]
        c_def = self.get_user_context(
            title='Сброс пароля', breadcrumb=breadcrumb)
        return {**context, **c_def}


class VersaPasswordResetConfirmView(DataMixin, auth_views.PasswordResetConfirmView):
    form_class = PasswordResetConfirmForm
    template_name = 'main/password-reset-confirm.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),
                      ('user-settings', _('Profile settings')),]
        c_def = self.get_user_context(breadcrumb=breadcrumb)
        return {**context, **c_def}


class VersaPasswordResetDoneView(DataMixin, auth_views.PasswordResetDoneView):
    template_name = 'main/password-reset-done.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),
                      ('user-settings', _('Profile settings')),]
        c_def = self.get_user_context(
            title='Письмо с инструкциями по восстановлению пароля отправлено',
            breadcrumb=breadcrumb
        )
        return {**context, **c_def}


class VersaPasswordResetCompleteView(DataMixin, auth_views.PasswordResetCompleteView):
    template_name = 'main/password-reset-complete.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        breadcrumb = [('personal-account', _('Personal account')),
                      ('user-settings', _('Profile settings')),]
        c_def = self.get_user_context(
            title='Восстановление пароля завершено',
            breadcrumb=breadcrumb
        )
        return {**context, **c_def}


# форма регистрации через админку с капчей
class VersaAdminLoginView(auth_views.LoginView):
    # шаблон находится вовсе не в этом приложении, до его поиска просто не доходит очередь
    # так как в settings указано, что сначала ищем все шаблоны в корне приложения: 'DIRS': [BASE_DIR / 'templates'],
    # по этому admin/login.html - это путь от корня проекта
    template_name = 'admin/login.html'
    form_class = LoginUserForm
