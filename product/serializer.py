from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ("name", "slug", "image", "price", "avg_rating")


class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ("id", "sold", "created_date", "modified_date", "category", "is_available")
        lookup_field = "slug"
        extra_kwargs = {"url": {"lookup_field": "slug"}}
