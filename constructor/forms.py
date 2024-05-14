from django import forms


class SimpleForm(forms.Form):
    pass


class ConstructorForm(forms.Form):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        initial = kwargs['initial']
        self.fields['types'].choices = initial['types_choices']
        self.fields['diameters'].choices = [('','- Условный диаметр, DN(мм) -')] + initial['diameters_choices']
        self.fields['pressures'].choices = [('', '- Рабочее давление, PN(Бар) -')]
        self.fields['lengths'].choices = [('','- Длина, L(мм) -')] + initial['lengths_choices']
        self.fields['fittings1'].choices = [('','- Группа концевой арматуры -')] + initial['fittings_choices']
        self.fields['fittings2'].choices = [('','- Группа концевой арматуры -')] + initial['fittings_choices']
        self.fields['fittingsA1'].choices = [('','- Группа концевой арматуры -')] + initial['fittings_choices']
        self.fields['fittingsA2'].choices = [('','- Группа концевой арматуры -')] + initial['fittings_choices']
        self.fields['materials1'].choices = [('', '- Материал -')] + initial['materials']
        self.fields['materials2'].choices = [('', '- Материал -')] + initial['materials']
        self.fields['materialsA1'].choices = [('', '- Материал -')] + initial['materials']
        self.fields['materialsA2'].choices = [('', '- Материал -')] + initial['materials']
        self.fields['typefitting1'].choices = [('', '- Концевая арматура -')]
        self.fields['typefitting2'].choices = [('', '- Концевая арматура -')]
        self.fields['typefittingA1'].choices = [('', '- Концевая арматура -')]
        self.fields['typefittingA2'].choices = [('', '- Концевая арматура -')]
        self.fields['innerscreen'].choices = [('', '- Внутренний экран -')]
        self.fields['outershells'].choices = [('', '- Наружная оболочка -')]
        self.fields['braid'].choices = [('', '- Оплетка -')]

    fittings1 = forms.ChoiceField(required=False,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorGroupsEndFittings1', }))
    materials1 = forms.ChoiceField(required=False,
                                   widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorMaterials1', }))
    typefitting1 = forms.ChoiceField(required=False,
                                     widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorTypeFitting1', }))
    fittingsA1 = forms.ChoiceField(choices=tuple(), required=False,
                                   widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorGroupsEndFittingsA1', }))
    materialsA1 = forms.ChoiceField(required=False,
                                    widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorMaterialsA1', }))
    typefittingA1 = forms.ChoiceField(required=False,
                                      widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorTypeFittingA1', }))
    fittings2 = forms.ChoiceField(required=False,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorGroupsEndFittings2', }))
    materials2 = forms.ChoiceField(required=False,
                                   widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorMaterials2', }))
    typefitting2 = forms.ChoiceField(required=False,
                                     widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorTypeFitting2', }))
    fittingsA2 = forms.ChoiceField(choices=tuple(), required=False,
                                   widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorGroupsEndFittingsA2', }))
    materialsA2 = forms.ChoiceField(required=False,
                                    widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorMaterialsA2', }))
    typefittingA2 = forms.ChoiceField(required=False,
                                      widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'constructorTypeFittingA2', }))
    types = forms.ChoiceField(choices=tuple(), label='Тип изделия', required=True,
                              widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1 d-inline-block border border-danger w-50', 'id': 'constructorTypes', }))
    diameters = forms.ChoiceField(choices=tuple(), required=True,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block border border-danger w-75', 'id': 'constructorDiameters', }))
    pressures = forms.ChoiceField(choices=tuple(), required=True,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block border border-danger w-75', 'id': 'constructorPressures', }))
    lengths = forms.ChoiceField(choices=tuple(), required=True,
                                widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block border border-danger w-75', 'id': 'constructorLengthsHoses', }))
    innerscreen = forms.ChoiceField(required=False,
                                    widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block w-75', 'id': 'constructorInnerScreen', }))
    outershells = forms.ChoiceField(required=False,
                                    widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block w-75', 'id': 'constructorOuterShells', }))
    braid = forms.ChoiceField(required=False,
                               widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block border border-danger w-75', 'id': 'constructorBraid', }))
    corrugation = forms.CharField(required=True,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block border border-danger w-75', 'id': 'constructorCorrugation', }))
    workspace = forms.CharField(max_length=100, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-sm d-inline-block w-75', 'id': 'constructorWorkSpace', 'placeholder': 'Рабочая среда', }))
    temperature = forms.CharField(max_length=100, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control form-control-sm d-inline-block w-75', 'id': 'constructorTemperature', 'placeholder': 'Т рабочей среды (°C)', }))
    radius = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-sm d-inline-block w-75', 'id': 'constructorRadius', 'placeholder': 'Радиус изгиба (мм)', }))
    mrсount = forms.CharField(max_length=4, label='Количество', required=False, initial=1,
                              widget=forms.TextInput(attrs={'class': 'form-control form-control-sm d-inline-block w-50', 'id': 'constructorCount', 'placeholder': 'Количество', }))
