from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/', views.display_article_overview, name='display_article_overview'),
    path('wiki/add-article/', views.add_article, name='add_article'),
    path('wiki/create-or-edit/', views.create_or_edit_article, name='create_or_edit_article'),
    path('wiki/<str:article_id>/edit/', views.edit_article, name='edit_article'),
    path('wiki/<str:article_id>/', views.display_detail, name='display_detail'),
    path('wiki/<str:article_id>/delete/', views.delete_article, name='delete_article')
]
