from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_page, name="news_page"),
    path('add_news', views.add_news, name="add_news")
]