from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializer import CategorySerializer
from django.core.cache import cache


@api_view(["GET"])
def get_categories(request):
    print("get_categories")
    cached_data = cache.get("categories")
    if cached_data:
        print("cache hit")
        return Response(cached_data)
    print("cache miss")
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    cache.set("categories", serializer.data, timeout=60 * 60 * 24)
    return Response(serializer.data)


@api_view(["GET"])
def get_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    print("get_category")
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)
