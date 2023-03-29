from django.urls import path,include
from product import views
urlpatterns = [
    path('', views.product_list,name="product_list"),
    path('find_product/', views.find_product,name="find_product"),
    path('add_product/', views.add_product,name="add_product"),
]
