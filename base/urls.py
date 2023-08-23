from django.contrib import admin
from django.urls import path, include
from apy.models import ProductResource, DishResource
from tastypie.api import Api

api = Api(api_name='v1')

dish_resource = DishResource()
product_resource = ProductResource()

api.register(dish_resource)
api.register(product_resource)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('menu.urls')),
    path('api/', include(api.urls)),


]
