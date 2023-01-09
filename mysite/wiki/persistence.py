from .models import Article
from django.shortcuts import get_object_or_404


def delete_article_if_exists(article_id):
    result = get_object_or_404(Article, article_id=article_id)
    result.delete()


def get_article_or_404(article_id):
    return get_object_or_404(Article, article_id=article_id) # not ideal to mix status code in persistence layer


def get_article(article_id):
    result = Article.objects.filter(article_id=article_id)
    if len(result) > 0:
        return result[0]
