# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import views
from django.conf.urls.static import static

urlpatterns = patterns('loja',
    # Examples:
    url(r'^$', 'views.index', name='index'),
    url(r'^lojas/(?P<id>\d+)/$', 'views.lojas', name='lojas'),
    
    
)
#to upload of files Muitos sites oferecem a seus usuários com a capacidade de fazer isso - por exemplo, para fazer o upload de uma imagem de perfil
