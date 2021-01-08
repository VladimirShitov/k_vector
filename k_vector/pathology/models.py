from django.db import models
from tinymce.models import HTMLField


class SampleCategory(models.Model):
    name = models.CharField(max_length=200, unique=True)

    @classmethod
    def get_all_categories(cls):
        return [category.name for category in cls.objects.all()]


class Sample(models.Model):
    title = models.CharField(max_length=512)
    category = models.ForeignKey(to=SampleCategory, on_delete=models.CASCADE)
    description = HTMLField(blank=True)


class SamplePhoto(models.Model):
    image = models.ImageField(upload_to="images/")
    order = models.IntegerField(unique=True)
    sample = models.ForeignKey(Sample, on_delete=models.CASCADE)
