from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer, ProductDetailsSerializer
from rest_framework import status

@api_view(["GET"])
def get_products(request):
    categories = request.GET.getlist("category")
    page = request.GET.get("page", 1)
    limit = request.GET.get("limit", 10)

    limit = int(limit)
    page = int(page)
    start_index = (page - 1) * limit
    end_index = page * limit

    if categories:
        products = Product.objects.filter(category__slug__in=categories).order_by(
            "-created_date"
        )[start_index:end_index]
    else:
        products = Product.objects.all().order_by("-created_date")[
            start_index:end_index
        ]

    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_product(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        return Response({"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductDetailsSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)
