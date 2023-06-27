from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Category
from .serializer import CategorySerializer


@api_view(["GET"])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def get_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    serializer = CategorySerializer(category, many=False)
    return Response(serializer.data)
