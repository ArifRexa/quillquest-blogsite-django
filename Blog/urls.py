from django.contrib import admin
from django.contrib.auth import views as auth_views
from .views import BlogPostUpdateView, BlogPostDeleteView
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogs , name='blogs'),
    path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('edit_blog/<int:pk>/', BlogPostUpdateView.as_view(), name='edit_blog'),
    path('blogs/delete/<int:pk>/', BlogPostDeleteView.as_view(), name='delete_blog'),

]