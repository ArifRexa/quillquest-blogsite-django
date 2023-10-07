from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('blogs/', include('Blog.urls')),
    path('profile/', views.profile, name='profile'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]