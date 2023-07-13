from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializer import CategorySerializer
from django.core.cache import cache
from django_ratelimit.decorators import ratelimit
from rest_framework import status


@api_view(["GET"])
@ratelimit(key="user_or_ip", rate="20/m", block=True)
def get_categories(request):
    cached_data = cache.get("categories")
    if cached_data:
        return Response(cached_data, status=status.HTTP_200_OK)

    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    cache.set("categories", serializer.data, timeout=100)
    return Response(serializer.data, status=status.HTTP_200_OK)
