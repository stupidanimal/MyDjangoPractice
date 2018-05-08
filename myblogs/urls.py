from django.urls import path
from . import views

app_name = 'myblogs'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_blog', views.add_blog, name='add_blog'),
    path('blog/<int:blog_id>', views.blog, name='blog'),
]
