from .models import News
from django.forms import ModelForm,TextInput, DateInput
from tinymce.widgets import TinyMCE


class NewsForm (ModelForm):
    class Meta:
        model = News
        fields = ['title', 'information', 'date', 'image']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'information': TinyMCE(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',

            }),
            'date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата публикации'
            })
        }

