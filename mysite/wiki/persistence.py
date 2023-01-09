from .models import Article
from django.shortcuts import get_object_or_404


def get_article_or_404(article_id):
    return get_object_or_404(Article, article_id=article_id)


def get_article(article_id):
    result = Article.objects.filter(article_id=article_id)
    if len(result) > 0:
        return result[0]
