from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer, ProductDetailsSerializer


@api_view(["GET"])
def get_products(request):
    print("get_products")
    products = Product.objects.all().order_by("-created_date")
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, product_slug):
    category = Product.objects.get(slug=product_slug)
    print("get_product")
    serializer = ProductDetailsSerializer(category, many=False)
    return Response(serializer.data)
