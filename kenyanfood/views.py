from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Food
from .serializer import FoodSerializer


# Create your views here.
@api_view(["GET"])
def get_food(request):
    food = Food.objects.all()
    serializer = FoodSerializer(food, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def post_food(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
