from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm


def news_page(request):
    news = News.objects.all()

    data={
        'news': news
    }
    return render(request, 'forum_page/news_page.html', data)


def add_news(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/news/')
        else:
            error = 'В форме содержится ошибка'

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'forum_page/add_news.html', data)
