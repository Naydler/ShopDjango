from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('api/allproducts', get_all_products),
    path('api/allproductsbycategory/<str:categorysearch>', get_all_products_by_category),
    path('api/allproductsbysize/<str:sizesearch>/', get_all_products_by_size),
    path('api/allproductsbyprice/<str:pricesearch>/', get_all_products_by_price),
    
    path('',product_list, name='products_list')
]