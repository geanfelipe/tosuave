# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, request, HttpResponseRedirect, HttpRequest
from django.template.response import TemplateResponse
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login , logout
from datetime import datetime
import django.utils.encoding
import os

# Create your views here.
def index(request):
	return HttpResponse("PORRA")