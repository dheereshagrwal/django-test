from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializer import CategorySerializer
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

from django_ratelimit.decorators import ratelimit

@api_view(["GET"])
@login_required
@ratelimit(key='user_or_ip', rate='2/m', block=True)
def get_categories(request):
    print("get_categories")
    print("request.user", request.user)
    # cached_data = cache.get("categories")
    # if cached_data:
    #     print("cache hit")
    #     return Response(cached_data)
    # print("cache miss")
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
