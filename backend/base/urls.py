from django.urls import path
from . import views

urlpatterns =[
    path("",views.getProducts,name="getproducts"),
    path("product/<int:id>",views.getProduct,name="getprodut")
]