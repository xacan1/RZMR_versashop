from django import forms
from blog.models import *


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'photo', 'text', 'is_published',]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Заголовок', 'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'placeholder': 'Введите текст статьи', 'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
