from django.template import loader

from .models import Article
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    latest_article_list = Article.objects.order_by('title')
    template = loader.get_template('wiki/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    # TODO redirection to /wiki
    return HttpResponse(template.render(context, request))


def add_article(request):
    template = loader.get_template('wiki/create-edit.html')
    context = {}
    return HttpResponse(template.render(context, request))


def create_or_edit_article(request):
    title, text = request.POST['title'], request.POST['text']
    article_id = '_'.join(title.lower().split())
    previous_article_id = request.POST['previous_article_id']
    result = Article.objects.filter(article_id=article_id)
    # tODO fetch a thing
    previous_result = Article.objects.filter(article_id=previous_article_id)
    if len(result) == 0:
        if len(previous_result) != 0:
            previous_result[0].delete()
        article = Article(title=title, article_id=article_id, text=text)
        article.save()
    else:
        article = result[0]
        article.title = title
        article.text = text
        article.save()
    return HttpResponseRedirect(f'/wiki/{article_id}')


def edit_article(request, article_id):
    article = Article.objects.filter(article_id=article_id)[0]
    template = loader.get_template('wiki/create-edit.html')
    context = {
        'article': article,
        'previous_article_id': article.article_id
    }
    return HttpResponse(template.render(context, request))


def display_detail(request, article_id):
    article = Article.objects.filter(article_id=article_id)[0]
    template = loader.get_template('wiki/detail.html')
    context = {
        'article': article
    }
    return HttpResponse(template.render(context, request))


def delete_article(request, article_id):
    article = Article.objects.filter(article_id=article_id)[0]
    article.delete()
    return HttpResponseRedirect('/wiki/')
