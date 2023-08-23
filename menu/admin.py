from django.contrib import admin
from .models import Dish, DishProduct, Product

admin.site.site_header = "Создание меню"
admin.site.site_title = "Menu"
admin.site.index_title = "Добро пожаловать в панель Администратора"


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'proteins', 'fats', 'carbohydrates')









admin.site.register(Dish)
admin.site.register(DishProduct)
admin.site.register(Product)
