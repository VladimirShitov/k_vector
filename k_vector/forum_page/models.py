from django.db import models
from tinymce.models import HTMLField


class News(models.Model):
    title = models.CharField(max_length=140)
    information = HTMLField(blank=True)
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title
