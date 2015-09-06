# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from django.core import serializers
import django.utils.encoding
from datetime import datetime
import os
import json
from models import Lojas,Produtos
from suave.decorators import ajax_login_required
# Create your views here.

"""
retorna uma lista de lojas
"""
@ajax_login_required
def lojas(request):

	lojas = serializers.serialize("json", Lojas.objects.all())

	#esse objeto é do tipo unicode
	if(lojas=='[]'): #se essa merda estiver vazia entao..
		return HttpResponse('{}',content_type="application/json")

	return HttpResponse(lojas,content_type="application/json")

"""
retorna uma loja especifica
"""
@ajax_login_required
def loja(request,id):

	loja = serializers.serialize("json", Lojas.objects.filter(pk=id))

	#esse objeto é do tipo unicode
	if(loja=='[]'): #se essa merda estiver vazia entao..
		return HttpResponse('{}',content_type="application/json")

	return HttpResponse(loja,content_type="application/json")


"""
retorna uma lista de produtos de uma loja
"""
@ajax_login_required
def produtos(request,id):

	loja = Lojas.objects.filter(pk=id)

	produtos = serializers.serialize("json",Produtos.objects.filter(loja=loja))

	#esse objeto é do tipo unicode
	if(produtos=='[]'): #se essa merda estiver vazia entao..
		return HttpResponse('{}',content_type="application/json")

	return HttpResponse(produtos,content_type="application/json")