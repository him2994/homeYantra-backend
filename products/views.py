# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

from products.models import Product
from products.serializers import ProductSerializer 
from products.filters import ProductFilter, filters


class ProductViewSet(viewsets.ModelViewSet):

	queryset = Product.objects.all()
	serializer_class = ProductSerializer
	permission_classes = [AllowAny]
	filter_backends = (filters.DjangoFilterBackend,)
	filter_class = ProductFilter
	lookup_field = 'model_name'
	# pagination_class = PageNumberPagination
