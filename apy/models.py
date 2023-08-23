from tastypie.resources import ModelResource
from menu.models import Dish, Product


class DishResource(ModelResource):
    class Meta:
        queryset = Dish.objects.all()
        resource_name = 'dishes'
        allowed_methods = ['get']


class ProductResource(ModelResource):
    class Meta:
        queryset = Product.objects.all()
        resource_name = 'products'
        allowed_methods = ['get', 'post', 'delete']

