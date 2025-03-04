from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django_recaptcha.fields import ReCaptchaField
from shop.models import *


class SimpleForm(forms.Form):
    captcha = ReCaptchaField()

    def send_email_for_call(self):
        name = self.data.get('name', '')
        phone = self.data.get('phone', '')

        send_mail(subject=f'Запрос на обратный звонок',
                  message=f'{name} просит перезвонить на номер: {phone}',
                  from_email=settings.EMAIL_USER,
                  recipient_list=[settings.COMPANY_EMAIL],
                  fail_silently=False)

    def send_email_for_feedback(self):
        name = self.data.get('name', '')
        phone = self.data.get('phone', '')
        email = self.data.get('email', '')
        question = self.data.get('question', '')

        send_mail(subject=f'Вопрос от посетителя сайта',
                  message=f'{name} спрашивает:\n{question}\nТелефон для связи: {phone}\nПочта для связи: {email}',
                  from_email=settings.EMAIL_USER,
                  recipient_list=[settings.COMPANY_EMAIL],
                  fail_silently=False)


# class RequestPhoneCallForm(forms.Form):
#   name = forms.CharField(widget=forms.TextInput(
#       attrs={'class': 'form-control', 'type': 'text', 'placeholder': 'Ваше имя'}), required=True)
#   phone = forms.IntegerField(widget=forms.NumberInput(
#       attrs={'class': 'form-control', 'type': 'tel', 'placeholder': 'Ваш телефон: 89012223344'}), required=True)
#   privacy = forms.BooleanField(label='*я соглашаюсь на обработку',
#                               widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=True)

#     def send_email(self):
#         name = self.data.get('name', '')
#         phone = self.data.get('phone', '')

#         send_mail(subject=f'Запрос на обратный звонок',
#                   message=f'{name} просит перезвонить на номер: {phone}',
#                   from_email=settings.EMAIL_USER,
#                   recipient_list=[settings.COMPANY_EMAIL],
#                   fail_silently=False)
