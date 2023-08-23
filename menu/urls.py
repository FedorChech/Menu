from django.urls import path
from . import views

urlpatterns = [
    path('create_menu/', views.create_menu, name='create_menu'),
    path('', views.create_breakfast, name='main'),
    # path('main_menu', views.main_menu, name='main_menu'),
    path('dish/<int:dish_id>/', views.dish_info, name='dish_info'),
    path('dish_list/', views.dish_list, name='dish_list'),
    path('product_info/<int:product_id>/', views.product_info, name='product_info'),
    path('dish_list/', views.dish_list_view, name='dish_list_view'),
    path('product_list/', views.product_list_view, name='product_list_view'),

    path('dish/1/', views.dish_info_view, name='dish_info_view'),
    path('product/1/', views.product_info, name='product_info_view'),

    path('add_dish/', views.create_dish, name='add_dish'),
    path('add_product/', views.add_product, name='add_product'),

    path('success_page/', views.success_pages, name='success_page'),
    path('delete_dish/', views.delete_dish, name='delete_dish'),
    path('delete_product/', views.delete_product, name='delete_product'),
    path('delete_success/', views.delete_success, name='delete_success'),

]
