from django.shortcuts import render, get_object_or_404, redirect
from django.utils.datetime_safe import datetime

from .models import *
# from django.db.models import Sum
from .forms import DishForm, DishProductFormSet, DeleteDishForm, DeleteProductForm, Product, AddProductForm, \
    BreakfastForm, DishProduct, SaveMenuDishAndProducts


# Представление


def create_breakfast(request):
    if request.method == 'POST':
        form = BreakfastForm(request.POST)
        if form.is_valid():
            selected_dishes = form.cleaned_data['dishes']
            dishes_with_products = []
            total_products = {}  # Словарь для хранения суммы продуктов
            for dish in selected_dishes:
                products = DishProduct.objects.filter(dish=dish)
                dishes_with_products.append({'dish': dish, 'products': products})
                for product in products:
                    SaveMenuDishAndProducts.objects.create(
                        dish=dish,
                        product=product.product,
                        grams=product.grams
                    )
                return redirect('create_menu')

    else:
        form = BreakfastForm()
        dishes_with_products = []
        total_products = {}

    return render(request, 'main.html',
                  {'form': form, 'dishes_with_products': dishes_with_products,
                   'total_products': total_products})


# def create_menu(request):
#     dishes = SaveMenuDishAndProducts.dish.all()
#     products = SaveMenuDishAndProducts.product.all()
#     grams = SaveMenuDishAndProducts.grams.all()
#
#     extension = {
#         'dishes': dishes,
#         'products': products,
#         'grams': grams,
#     }
#
#     return render(request, 'create_menu.html', extension)


def create_menu(request):
    products_menu = []
    dishes_menu = []
    products_list = Product.objects.all()

    # Получение блюд и продуктов, созданных в последнюю минуту
    recently_created_items = SaveMenuDishAndProducts.objects.get_recently_created_items()

    for item in recently_created_items:
        if item.dish not in dishes_menu:
            dishes_menu.append(item.dish)

        if item.product not in products_menu:
            products_menu.append(item.product)

    extension = {
        'products_menu': products_menu,
        'products_list': products_list,
        'recently_created_items': recently_created_items,
        'dishes_menu': dishes_menu,
    }

    return render(request, 'create_menu.html', extension)





def dish_info(request, dish_id):
    dish = Dish.objects.get(pk=dish_id)
    products = get_products_for_dish(dish_id)
    total_calories = calculate_total_calories(dish_id)
    total_weight = calculate_total_weight(dish_id)
    prod_length_plus_one = len(products) + 1
    dish_p = get_object_or_404(Dish, pk=dish_id)
    products_all = dish.dishproduct_set.all()

    extension = {

        'prod_length_plus_one': prod_length_plus_one,
        'total_weight': total_weight,
        'total_calories': total_calories,
        'products': products,
        'dish': dish,
        'products_all': products_all,
        'dish_p': dish_p,
        'next_dish_id': next_dish_id,
        'previos_dish_id': previos_dish_id

    }
    return render(request, 'dish_info.html', extension)


def product_info(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product_info.html', {'product': product})


def dish_list(request):
    dishes = Dish.objects.all()
    extension = {
        'dishes': dishes,
    }
    return render(request, 'dish_list.html', extension)


def calculate_total_weight(dish_id):
    total_weight = DishProduct.objects.filter(dish_id=dish_id).aggregate(total=models.Sum('grams'))['total']
    return total_weight


def calculate_total_calories(dish_id):
    total_calories = DishProduct.objects.filter(dish_id=dish_id).aggregate(total=models.Sum('product__calories'))[
        'total']
    return total_calories


def get_products_for_dish(dish_id):
    dish_products = DishProduct.objects.filter(dish_id=dish_id)
    products = [dp.product for dp in dish_products]
    return products


def dish_list_view(request):
    return render(request, 'dish_list.html')


def product_list_view(request):
    products = Product.objects.all()
    extension = {
        'products': products
    }
    return render(request, 'product_list.html', extension)


def dish_info_view(request):
    return render(request, 'dish_info.html')


def success_pages(request):
    return render(request, 'success_page.html')


def delete_dish(request):
    return render(request, 'delete_dish.html')


def create_dish(request):
    if request.method == 'POST':
        dish_form = DishForm(request.POST)
        dish_product_formset = DishProductFormSet(request.POST)

        if dish_form.is_valid() and dish_product_formset.is_valid():
            dish = dish_form.save()
            instances = dish_product_formset.save(commit=False)
            for instance in instances:
                instance.dish = dish
                instance.save()
            return redirect('dish_list')  # Redirect to the same page to clear the form
    else:
        dish_form = DishForm()
        dish_product_formset = DishProductFormSet()

    return render(request, 'add_dish.html', {
        'dish_form': dish_form,
        'dish_product_formset': dish_product_formset,
    })


def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            calories = form.cleaned_data['calories']
            proteins = form.cleaned_data['proteins']
            fats = form.cleaned_data['fats']
            carbohydrates = form.cleaned_data['carbohydrates']
            new_product = Product.objects.create(name=name, calories=calories, proteins=proteins, fats=fats,
                                                 carbohydrates=carbohydrates)
            return redirect('product_list_view')  # Перенаправление после успешного добавления
    else:
        form = AddProductForm()

    return render(request, 'add_product.html', {'form': form})


def delete_dish(request):
    if request.method == "POST":
        form = DeleteDishForm(request.POST)
        if form.is_valid():
            dish = form.cleaned_data['dish']
            DishProduct.objects.filter(dish=dish).delete()
            dish.delete()
            return redirect('dish_list')  # Перенаправление на страницу успешного удаления
    else:
        form = DeleteDishForm()

    return render(request, 'delete_dish.html', {'form': form})


def delete_product(request):
    if request.method == "POST":
        form = DeleteProductForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data['product']
            DishProduct.objects.filter(product=product).delete()
            product.delete()
            return redirect('product_list_view')  # Перенаправление на страницу успешного удаления
    else:
        form = DeleteProductForm()

    return render(request, 'delete_product.html', {'form': form})


def delete_success(request):
    return render(request, 'delete_success.html')
