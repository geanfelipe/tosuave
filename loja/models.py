# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models import permalink
import datetime


class Lojas(models.Model):
	nome = models.CharField(max_length=128, unique=True,db_index=True)
	endereco = models.CharField(max_length=256)	
	numero = models.IntegerField()
	CEP = models.CharField(max_length=128)
	complemento = models.CharField(max_length=256)

	def __unicode__(self):
		return self.nome

class Produtos(models.Model):
	nome = models.CharField(max_length=128,unique=True,db_index=True)
	quantidade = models.IntegerField()
	preco = models.FloatField()
	loja = models.ForeignKey("Lojas")

	def __unicode__(self):
		return self.nome