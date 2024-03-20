from django import forms


class SimpleForm(forms.Form):
    pass


class ConstructorForm(forms.Form):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        initial = kwargs['initial']
        self.fields['types'].choices = initial['types_choices']
        self.fields['diameters'].choices = initial['diameters_choices']
        self.fields['pressures'].choices = initial['pressures_choices']
        self.fields['lengths'].choices = initial['lengths_choices']
        self.fields['fittings1'].choices = initial['fittings_choices']
        self.fields['fittings2'].choices = initial['fittings_choices']


    fittings1 = forms.ChoiceField(required=False,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'GroupsEndFittings1', }))
    materials1 = forms.ChoiceField(required=False,
                                   widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'Materials1', }))
    typefitting1 = forms.ChoiceField(required=False,
                                     widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'TypeFitting1', }))
    fittingsA1 = forms.ChoiceField(choices=tuple(), required=False,
                                   widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'GroupsEndFittingsA1', }))
    materialsA1 = forms.ChoiceField(required=False,
                                    widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'MaterialsA1', }))
    typefittingA1 = forms.ChoiceField(required=False,
                                      widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'TypeFittingA1', }))
    fittings2 = forms.ChoiceField(required=False,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'GroupsEndFittings2', }))
    materials2 = forms.ChoiceField(required=False,
                                   widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'Materials2', }))
    typefitting2 = forms.ChoiceField(required=False,
                                     widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1', 'id': 'TypeFitting2', }))

    types = forms.ChoiceField(choices=tuple(), label='Тип изделия', required=True,
                              widget=forms.Select(attrs={'class': 'form-select form-select-sm mb-1 d-inline-block border border-danger w-50', 'id': 'Types', }))
    diameters = forms.ChoiceField(choices=tuple(), required=True,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block border border-danger w-75', 'id': 'Diameters', }))
    pressures = forms.ChoiceField(choices=tuple(), required=True,
                                  widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block border border-danger w-75', 'id': 'Pressures', }))
    lengths = forms.ChoiceField(choices=tuple(), required=True,
                                widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block border border-danger w-75', 'id': 'LengthsHoses', }))
    innerscreen = forms.ChoiceField(required=False,
                                    widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block w-75', 'id': 'InnerScreen', }))
    outershells = forms.ChoiceField(required=False,
                                    widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block w-75', 'id': 'OuterShells', }))
    braids = forms.ChoiceField(required=False,
                               widget=forms.Select(attrs={'class': 'form-select form-select-sm d-inline-block w-75', 'id': 'Braids', }))
    workspace = forms.CharField(max_length=100, required=False,
                                widget=forms.TextInput(attrs={'class': 'form-control form-control-sm d-inline-block w-75', 'id': 'WorkSpace', 'placeholder': 'Рабочая среда', }))
    temperature = forms.CharField(max_length=100, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control form-control-sm d-inline-block w-75', 'id': 'Temperature', 'placeholder': 'Т рабочей среды (°C)', }))
    radius = forms.CharField(max_length=100, required=False,
                             widget=forms.TextInput(attrs={'class': 'form-control form-control-sm d-inline-block w-75', 'id': 'Radius', 'placeholder': 'Радиус изгиба (мм)', }))
    mrсount = forms.CharField(max_length=4, label='Количество', required=False,
                              widget=forms.TextInput(attrs={'class': 'form-control form-control-sm d-inline-block w-50', 'id': 'mrCount', 'placeholder': 'Количество', }))
