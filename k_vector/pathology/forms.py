from django import forms
from django.shortcuts import get_object_or_404
import floppyforms
from tinymce.widgets import TinyMCE

from .models import Sample, SampleCategory

TEXT_INPUTS_CLASS = "wide-text-input"


class SampleForm(forms.Form):
    title = forms.CharField(
        max_length=512,
        label="Название препарата",
        widget=forms.TextInput(attrs={"class": TEXT_INPUTS_CLASS})
    )
    category = forms.CharField(
        max_length=200,
        widget=floppyforms.widgets.Input(
            datalist=SampleCategory.get_all_categories(),
            attrs={"class": TEXT_INPUTS_CLASS}
        ),
        label="Категория"
    )
    description = forms.CharField(
        widget=TinyMCE(attrs={"class": TEXT_INPUTS_CLASS}),
        label="Описание"
    )
    images = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"multiple": True, "class": TEXT_INPUTS_CLASS}),
        label="Изображения"
    )


class SampleEditForm(forms.Form):
    title = forms.CharField(
        max_length=512,
        label="Название препарата",
        widget=forms.TextInput(attrs={"class": TEXT_INPUTS_CLASS})
    )
    category = forms.CharField(
        max_length=200,
        widget=floppyforms.widgets.Input(
            datalist=SampleCategory.get_all_categories(), attrs={"class": TEXT_INPUTS_CLASS}
        ),
        label="Категория",
    )
    description = forms.CharField(widget=TinyMCE(), label="Описание")

    def save(self, sample_id: int):
        sample = get_object_or_404(Sample, pk=sample_id)
        sample.title = self.cleaned_data["title"]
        sample.category, _ = SampleCategory.objects.get_or_create(name=self.cleaned_data["category"])
        sample.description = self.cleaned_data["description"]
        sample.save()
