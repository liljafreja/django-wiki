from django.template import loader

from .models import Article
from django.http import HttpResponse, HttpResponseRedirect

from .persistence import get_article_or_404, get_article


def index(_):
    return HttpResponseRedirect('/wiki')


def display_article_overview(request):
    latest_article_list = Article.objects.order_by('title')
    template = loader.get_template('wiki/index.html')
    context = {
        'latest_article_list': latest_article_list,
    }
    return HttpResponse(template.render(context, request))


def add_article(request):
    template = loader.get_template('wiki/create-edit.html')
    context = {}
    return HttpResponse(template.render(context, request))


def create_or_edit_article(request):
    title, text = request.POST['title'], request.POST['text']
    article_id = '_'.join(title.lower().split())
    article = get_article(article_id)
    if article is None:
        previous_article_id = request.POST['previous_article_id']
        previous_article = get_article(previous_article_id)
        if previous_article is not None:
            previous_article.delete()
        article = Article(title=title, article_id=article_id, text=text)
        article.save()
    else:
        article.title, article.text = title, text
        article.save()
    return HttpResponseRedirect(f'/wiki/{article_id}')


def edit_article(request, article_id):
    article = get_article(article_id)
    template = loader.get_template('wiki/create-edit.html')
    context = {
        'article': article,
        'previous_article_id': article.article_id
    }
    return HttpResponse(template.render(context, request))


import re


def render_custom_links(text):
    return re.sub(r'\[(.*)\]\((.*)\)',
                  lambda match: f'<a href="/wiki/{match.group(1)}">{match.group(2)}</a>', text)


def display_detail(request, article_id):
    article = get_article_or_404(article_id)
    template = loader.get_template('wiki/detail.html')
    context = {
        'article': article,
        'text': render_custom_links(article.text)
    }
    return HttpResponse(template.render(context, request))


def delete_article(_, article_id):
    article = get_article_or_404(article_id)
    article.delete()
    return HttpResponseRedirect('/wiki/')
