from django.views.generic import ListView
from django.shortcuts import render
import json
from .models import Article


def articles_list(request):
    template_name = 'articles/news.html'
    path = 'articles.json'

    with open(path, 'r') as jsonfile:
        data = json.loads(jsonfile.read())
        for line in data:
            if Article.objects.filter(id=line['pk']):
                pass
            else:
                Article.objects.create(title=line['fields']['title'],
                                     text=line['fields']['text'],
                                     published_at=line['fields']['published_at'],
                                     image=line['fields']['image']
                                     )
    articles = Article.objects.select_related('author', 'genre').order_by("-published_at")
    context = {
        'object_list': articles,
    }
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template_name, context)
