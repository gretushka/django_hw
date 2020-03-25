from django.views.generic import ListView
from django.shortcuts import render
import json

from articles.models import Article,Scope,Topic


def articles_list(request):
    template = 'articles/news.html'
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
    context = {
        'object_list':Article.objects.order_by("-published_at"),
    }

    return render(request, template, context)
