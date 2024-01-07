from django.urls import path
from .views import article_list, article_detail, article_create, article_create_form, article_edit, article_delete

app_name = 'article'

urlpatterns = [
    path('', article_list, name='article_list'),
    path('article/<slug:slug>/', article_detail, name='article_detail'),
    path('artcile/create/', article_create, name='create'),
    path('article/create/form/', article_create_form, name='create-form'),
    path('article/change/<int:pk>/', article_edit, name='change'),
    path('article/delete/<int:pk>/', article_delete, name='delete'),
]