from django import forms
from django.utils.translation import gettext_lazy as _
from shop.models import *


class SimpleForm(forms.Form):
    pass


class ProductListForm(forms.Form):
    SORT_CHOICES = (('price_asc', _('low-priced first')), ('price_desc', _('high-priced first')),
                    ('alphabet_asc', _('Sort alphabetically from A to Z')), ('alphabet_desc', _('Sort alphabetically from Z to A')),)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        initial = kwargs['initial']
        min_price = initial.get('price__min', 0)
        max_price = initial.get('price__max', 0)
        step_price = round((max_price - min_price) / 100, -2)

        get_params = initial['get_params']
        current_price = get_params.get('price_range_max', max_price)

        # Установлю цены от минимальной цены по отобранным товарам до максимальной
        self.fields['price_range_max'].widget.attrs['min'] = min_price
        self.fields['price_range_max'].widget.attrs['max'] = max_price
        self.fields['price_range_max'].widget.attrs['step'] = step_price if step_price < 100 else 100
        self.fields['price_range_max'].widget.attrs['value'] = current_price
        self.fields['current_price'].widget.attrs['placeholder'] = current_price

        # Найду и установлю значение из кортежа сортировки по значению sorting в GET параметрах, ведь именно оно прилетело нам из прошлого запроса пользователя
        if 'sorting' in get_params:
            self.fields['sorting'].initial = [
                choice[0] for choice in self.SORT_CHOICES if choice[0] == get_params['sorting']]

        # этот параметр-костыль нужен для нумерации групп атрибутов (слева на форме фильтрации) для аккордеона Bootstrap5, я его передаю в свойстве "help_text"
        accordion_id = 0

        # Динамически создам поля атрибутов товаров, ведь сайт не знает что за товары
        for attribute, values in initial['attribute_groups'].items():
            # Создам скрытое поле только ради Label что бы отобразить имя атрибута в группировке и не создавать кастомное поле для этой формы
            accordion_id += 1
            self.fields[attribute] = forms.CharField(label=attribute,
                                                     help_text=str(
                                                         accordion_id),
                                                     widget=forms.HiddenInput())

            for value in values:
                name = str(value['pk'])
                attrs = {'class': 'form-check-input',
                         'value': attribute, 'id': f'flexCheck{name}', }

                # Если параметр содержится в GET запросе, то на нем стоит галочка, значит пометим его при повторном вызове формы
                if name in get_params:
                    attrs['checked'] = ''

                self.fields[name] = forms.BooleanField(label=value['string_value'],
                                                       help_text=str(
                                                           accordion_id),
                                                       widget=forms.CheckboxInput(attrs=attrs), required=False)

    price_range_max = forms.IntegerField(widget=forms.NumberInput(
        attrs={'class': 'form-range', 'type': 'range', 'name': 'price_range_max', 'onchange': 'rangePrimary.value=value'})
    )
    current_price = forms.IntegerField(widget=forms.TextInput(
        attrs={'id': 'rangePrimary', 'readonly': '', 'form': ''}),
        required=False
    )
    sorting = forms.ChoiceField(
        label=_('Sort by:'),
        choices=SORT_CHOICES,
        widget=forms.Select(attrs={
                            'class': 'form-control', 'id': 'selectSorting', 'form': 'filtersAttributes'}),
        # initial=[choice[0] for choice in SORT_CHOICES]
    )


class AddOrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        initial = kwargs['initial']
        self.user = initial.get('user', None)

        if self.user:
            self.fields['company'].queryset = self.user.get_contractors.all()
            self.fields['company'].label = 'Выберите организацию для счета (если требуется выписать на юрлицо)'
        else:
            self.fields['company'].choices = []
            self.fields['company'].widget = forms.Select(attrs={'class': 'form-control d-none'})
            self.fields['company'].label = ''

        self.fields['payment_type'].empty_label = 'Не выбран вид оплаты'
        self.fields['payment_type'].queryset = PaymentType.objects.filter(use=True)
        self.fields['delivery_type'].empty_label = 'Не выбран способ получения'
        self.fields['company'].empty_label = 'Не указывать компанию'

    def clean_phone(self):
        phone = self.cleaned_data['phone']

        if len(phone) != 11 or not phone.isdigit() or phone[0] != '7':
            raise forms.ValidationError('Введите правильный мобильный номер')

        return phone

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'phone', 'email', 'address',
                  'comment', 'delivery_type', 'payment_type', 'coupon', 'company',]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'Электронная почта', 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Пример: 79001234567', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Пример: Уфа, ул. Ленина, дом 1', 'class': 'form-control'}),
            'payment_type': forms.Select(attrs={'class': 'form-control'}),
            'delivery_type': forms.Select(attrs={'class': 'form-control'}),
            'company': forms.Select(attrs={'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'cols': 60, 'rows': 3, 'class': 'form-control'}),
        }


class AddContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['name', 'full_name', 'inn', 'kpp',
                  'registered_address', 'actual_address',]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Наименование', 'class': 'form-control'}),
            'full_name': forms.TextInput(attrs={'placeholder': 'Официальное наименование', 'class': 'form-control'}),
            'inn': forms.TextInput(attrs={'placeholder': 'ИНН', 'class': 'form-control'}),
            'kpp': forms.TextInput(attrs={'placeholder': 'КПП', 'class': 'form-control'}),
            'registered_address': forms.TextInput(attrs={'placeholder': 'Юридический адрес', 'class': 'form-control'}),
            'actual_address': forms.TextInput(attrs={'placeholder': 'Фактический адрес', 'class': 'form-control'}),
        }
