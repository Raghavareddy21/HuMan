"""Hunger_Management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from HuMan import views

urlpatterns = [
    path('admin/', admin.site.urls),
     path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/',views.signup, name='signup'),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('about/',TemplateView.as_view(template_name='about-us.html'),name='about'),
    path('maps/',TemplateView.as_view(template_name='maps.html'),name='maps'),
    path('geocoding/',TemplateView.as_view(template_name='geocoding.html'),name='geocodeing'),
    path('login/',views.user_login,name="login"),
    path('logout/', views.user_logout, name="logout"),
    path('collect/',TemplateView.as_view(template_name='collect.html'),name='collect'),
    path('collects/',TemplateView.as_view(template_name='collects.html'),name='collects'),
]
