"""
URL configuration for talkClub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from appMy.views import *
from appMy.views import Comment
from django.urls import path

# from appMy.views import login, register, logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index ,name='main'),
    path('question/',Question,name='question'),
    path('post/',Post,name='post'),
    path('tinymce/', include('tinymce.urls')),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('comment/<slug>/', Comment, name='comment'),

    
]

