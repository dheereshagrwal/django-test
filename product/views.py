from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Product
from .serializer import ProductSerializer, ProductDetailsSerializer


@api_view(["GET"])
def get_products(request):
    print("get_products")

    # Check if category is provided

    categories = request.GET.getlist("category")

    # Retrieve the page number from the request
    page = request.GET.get("page")
    limit = request.GET.get("limit")
    if not page:
        page = 1
    if not limit:
        limit = 10

    limit = int(limit)
    page = int(page)
    # Calculate the start and end index based on the page number
    start_index = (page - 1) * limit
    end_index = page * limit
    print(start_index, end_index)

    if categories:
        products = Product.objects.filter(category__slug__in=categories).order_by(
            "-created_date"
        )[start_index:end_index]
    else:
        products = Product.objects.all().order_by("-created_date")[
            start_index:end_index
        ]

    serializer = ProductSerializer(products, many=True)

    # Return serialized data
    return Response(serializer.data)


@api_view(["GET"])
def get_product(request, product_slug):
    category = Product.objects.get(slug=product_slug)
    print("get_product")
    serializer = ProductDetailsSerializer(category, many=False)
    return Response(serializer.data)
