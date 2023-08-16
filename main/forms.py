from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import get_user_model


User = get_user_model()


class SimpleForm(forms.Form):
    pass


class FeedbackForm(forms.Form):
    title = forms.CharField(max_length=100, label='Заголовок',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(widget=forms.Textarea(
        attrs={'cols': 60, 'rows': 10, 'class': 'form-control'}), label='Текст сообщения')
    select = forms.ChoiceField(
        choices=(
            (1, 'Безнадежно'), (2, 'Плохо'), (3, 'Сойдет'), (4, 'Хорошо, но...'),
            (5, 'Отлично! Куда деньги закинуть?')
        ),
        label='Оценка сайта', widget=forms.Select(attrs={'class': 'form-select'}))
    # captcha = ReCaptchaField()


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повторите пароль',
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ('email', 'phone', 'first_name', 'last_name')
        widgets = {'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'first_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'last_name': forms.TextInput(attrs={'class': 'form-control'}),
                   'phone': forms.TextInput(attrs={'class': 'form-control'})}


class LoginUserForm(AuthenticationForm):
    username = forms.EmailField(
        label='Адрес электронной почты', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    # captcha = ReCaptchaField()
    # fields = ('email', 'password')
    # widgets = {'email': forms.EmailInput(attrs={'class': 'form-input'}),
    #            'password': forms.PasswordInput(attrs={'class': 'form-input'})}


class VersaPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label='Старый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label='Подтверждение нового пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class VersaPasswordResetForm(PasswordResetForm):
    email = forms.CharField(
        label='Адрес электронной почты',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )


class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='Новый пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    new_password2 = forms.CharField(
        label='Подтверждение нового пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
