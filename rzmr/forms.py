from django import forms
from django.conf import settings
from django.core.mail import send_mail
from shop.models import *


class SimpleForm(forms.Form):
    def send_email(self):
        name = self.data.get('name', '')
        phone = self.data.get('phone', '')

        send_mail(subject=f'Запрос на обратный звонок',
                  message=f'{name} просит перезвонить на номер: {phone}',
                  from_email=settings.EMAIL_USER,
                  recipient_list=[settings.COMPANY_EMAIL],
                  fail_silently=False)


# class RequestPhoneCallForm(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ваше имя'}), required=True)
#     phone = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Ваш телефон'}), required=True)
#     privacy = forms.BooleanField(label='*я соглашаюсь на обработку', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}), required=True)

#     def send_email(self):
#         print(self.cleaned_data)
