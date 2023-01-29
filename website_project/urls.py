"""website_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from App import views


urlpatterns = [
    # system
    path('admin/', admin.site.urls),

    # index
    path('', views.index, name='index'),

    # profile
    path('profile/', views.profile_page, name='profile'),
    path('profile/edit/', views.profile_editing, name='profile_edit'),

    # login and signin
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # votings
    path('votings/details_template/', views.voting_page_template, name='voting_details'),
    path('votings/create/', views.make_voting, name='voting_create'),

]
