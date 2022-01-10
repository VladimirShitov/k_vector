from .models import News
from django.forms import ModelForm, TextInput, Textarea, DateInput


class NewsForm (ModelForm):
    class Meta:
        model = News
        fields = ['news_title', 'news_information', 'news_date', 'news_image']

        widgets = {
            'news_title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),
            'news_information': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),
            'news_date': DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата публикации'
            })
        }