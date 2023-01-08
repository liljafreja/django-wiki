from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    article_id = models.CharField(max_length=255, unique=True)
    text = models.TextField()


