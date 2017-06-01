# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Product(models.Model):
	title		=	models.CharField(max_length=100, unique=True)
	model_name	=	models.CharField(max_length=20, unique=True)
	description	=	models.CharField(max_length=500, blank=True, null=True)
	price		=	models.IntegerField()
	mrp			=	models.IntegerField()
	img_hash	=	models.CharField(max_length=500)
	brand		=	models.CharField(max_length=30, db_index=True)
	primary_img	=	models.IntegerField()
	pcategory	=	models.CharField(max_length=30, db_index=True)
	scategory	=	models.CharField(max_length=30, db_index=True)
	features 	=	models.CharField(max_length=1000, blank=True, null=True)

	class Meta:
		db_table = 'products'

	def __str__(self):
		return self.model_name

	