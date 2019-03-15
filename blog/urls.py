
from django.urls import path
from . import views
app_name='blog'
urlpatterns = [

    path('index/', views.index),
    path('article/<int:article_id>/', views.article_page,name='article_page'),
    # 使用django2.0提供的path转换器，直接使用‘<>’捕获值，例如<int:article_id>，需指定类型
    path('edit/<int:article_id>/', views.edit_page,name='edit_page'),
    path('edit/action/', views.edit_action,name='edit_action'),
]
