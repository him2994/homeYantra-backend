from __future__ import unicode_literals

from django_filters import rest_framework as filters
from django_filters import Filter
from django_filters.fields import Lookup
import django_filters

from products.models import Product


class ListFilter(Filter):
  def filter( self, qs, value ):
    return super( ListFilter, self ).filter( qs, Lookup( value.split( u"," ), "in") )


class ProductFilter(filters.FilterSet):
	min_price	=	django_filters.NumberFilter(name='price', lookup_expr='gte')
	max_price	=	django_filters.NumberFilter(name='price', lookup_expr='lte')
	pcategory	=	ListFilter(name='pcategory')
	scategory	=	ListFilter(name='scategory')
	brand 		=	ListFilter(name='brand')

	class Meta:
		model = Product
		fields = ['pcategory', 'scategory', 'min_price', 'max_price', 'brand']

