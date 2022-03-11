from django.db import models
from tinymce.models import HTMLField


class News(models.Model):
    news_title = models.CharField(max_length=140)
    news_information = HTMLField(blank=True)
    news_date = models.DateTimeField()
    news_image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.news_title
