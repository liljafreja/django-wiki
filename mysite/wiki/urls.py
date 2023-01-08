from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.add_article, name='new'),
    path('create/', views.create_article, name='create'),
    path('wiki/<str:article_id>/', views.display_detail, name='display_detail')
]
