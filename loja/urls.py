# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
import views
from django.conf.urls.static import static

urlpatterns = patterns('loja',
    # Examples:
    url(r'^lojas/$', 'views.lojas', name='lojas'), #TRAZ UMA LISTA DE LOJAS
    url(r'^lojas/(?P<id>\d+)/$', 'views.loja', name='loja'), #TRAZ UMA LOJA ESPECIFICA
    url(r'^produtos/(?P<id>\d+)/$', 'views.produtos', name='produtos'), #TRAZ PRODUTOS DE UMA LOJA
    
)