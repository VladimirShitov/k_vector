from .models import News
from django.forms import ModelForm,TextInput, DateInput
from tinymce.widgets import TinyMCE


class NewsForm (ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_information', 'news_date', 'news_image']

        widgets = {
            'news_title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'news_information': TinyMCE(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи',

            }),
            'news_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата публикации'
            })
        }

