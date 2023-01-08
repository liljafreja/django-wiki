from django.template import loader

from .models import Article
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    latest_article_list = Article.objects.order_by('title')
    template = loader.get_template('wiki/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))


def add_article(request):
    template = loader.get_template('wiki/new.html')
    context = {}
    return HttpResponse(template.render(context, request))


def create_article(request):
    article = Article()
    title = request.POST['title']
    text = request.POST['text']
    article.title = title
    article.text = text
    article.article_id = '_'.join(title.lower().split())
    article.save()
    return HttpResponseRedirect(f'/wiki/{article.article_id}')


def display_detail(request, article_id):
    article = Article.objects.filter(article_id=article_id)[0]
    template = loader.get_template('wiki/detail.html')
    context = {
        'article': article
    }
    return HttpResponse(template.render(context, request))
