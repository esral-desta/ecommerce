from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from .Products import Products

from .serializers import ProductSerializer
# Create your views here.

from .models import *


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    products = ProductSerializer(products,many=True)
    return Response(products.data)

@api_view(['GET'])
def getProduct(request,id):
    product = Product.objects.filter(id=id)[0]
    product = ProductSerializer(product,many=False)
    return Response(product.data)
