from django.urls import path
from .views import (
					product_home, 
					product, 
					product_detail, 
					add_product, 
					edit_product, 
					delete_product,
					about,
					contact
					)

app_name = "shop"
urlpatterns = [
    path('', product_home, name="shop"),
    path('products/', product, name="products"),
    path('products/<int:pk>/', product_detail, name="detail"),
    path('products/add/', add_product, name="add"),
    path('products/edit/<int:pk>/', edit_product, name="edit"),
    path('products/delete/<int:pk>/', delete_product, name="delete"),
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
]