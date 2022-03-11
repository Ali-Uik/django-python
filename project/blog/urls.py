from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:pk>', category_list, name='category_list'),
    path('article/<int:pk>', article_detail, name='article_detail'),
    path('new/', add_article, name='add_article'),

    # Пути на классах
    path('', ArticleList.as_view(), name='index')
]
