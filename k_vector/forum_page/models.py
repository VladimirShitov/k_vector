from django.db import models


class News(models.Model):
    news_title = models.CharField(max_length=140)
    news_information = models.TextField()
    news_date = models.DateTimeField()
    news_image = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.news_title
