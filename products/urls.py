from django.conf.urls import url

from products.viewsets import ProductList, ProductDetails


urlpatterns = [
    url(r'^(?P<model_name>[\w.@+-]+)/$', ProductDetails, name='product_details'),
    url(r'^$', ProductList, name='product_list'),
]
