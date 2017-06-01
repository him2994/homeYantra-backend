from __future__ import unicode_literals

from products.views import ProductViewSet


ProductList = ProductViewSet.as_view({
	'get': 'list',
	'post': 'create'
})

ProductDetails = ProductViewSet.as_view({
	'get': 'retrieve'
})