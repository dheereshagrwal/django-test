from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Cart, CartItem
from product.models import Product
from .serializer import CartSerializer, CartItemSerializer

from rest_framework import status


@api_view(["GET"])
def get_cart(request, cart_id):
    if not cart_id:
        return Response(
            {"detail": "Cart ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_cart(request, cart_id):
    if not cart_id:
        return Response(
            {"detail": "Cart ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        cart = Cart.objects.create(cart_id=cart_id)
    except:
        return Response(
            {"detail": "Cart with this ID already exists"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["DELETE"])
def clear_cart(request, cart_id):
    if not cart_id:
        return Response(
            {"detail": "Cart ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    cart_items = CartItem.objects.filter(cart=cart)
    cart_items.delete()
    return Response({"detail": "Cart cleared"}, status=status.HTTP_204_NO_CONTENT)


@api_view(["GET"])
def get_cart_items(request, cart_id):
    if not cart_id:
        return Response(
            {"detail": "Cart ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    cart_items = CartItem.objects.filter(cart=cart)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def add_cart_item(request, cart_id, product_slug):
    print(cart_id, product_slug)
    if not cart_id:
        return Response(
            {"detail": "Cart ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if not product_slug:
        return Response(
            {"detail": "Product slug is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        return Response(
            {"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        cart_item = CartItem.objects.create(cart=cart, product=product, quantity=1)
    except IntegrityError:
        return Response(
            {"detail": "Item already in cart"}, status=status.HTTP_400_BAD_REQUEST
        )

    return Response({"detail": "Item added to cart"}, status=status.HTTP_201_CREATED)


@api_view(["PATCH"])
def update_cart_item(request, cart_id, product_slug):
    quantity = request.GET.get("quantity")
    if not quantity:
        return Response(
            {"detail": "Quantity is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not quantity.isdigit():
        return Response(
            {"detail": "Quantity must be a number"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not cart_id:
        return Response(
            {"detail": "Cart ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not product_slug:
        return Response(
            {"detail": "Product slug is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        return Response(
            {"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
    except CartItem.DoesNotExist:
        return Response(
            {"detail": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND
        )

    if quantity is not None:
        cart_item.quantity = quantity
        cart_item.save()

    return Response({"detail": "Cart updated"}, status=status.HTTP_200_OK)


@api_view(["DELETE"])
def remove_cart_item(request, cart_id, product_slug):
    if not cart_id:
        return Response(
            {"detail": "Cart ID is required"}, status=status.HTTP_400_BAD_REQUEST
        )
    if not product_slug:
        return Response(
            {"detail": "Product slug is required"}, status=status.HTTP_400_BAD_REQUEST
        )

    try:
        cart = Cart.objects.get(cart_id=cart_id)
    except Cart.DoesNotExist:
        return Response({"detail": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

    try:
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        return Response(
            {"detail": "Product not found"}, status=status.HTTP_404_NOT_FOUND
        )

    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
    except CartItem.DoesNotExist:
        return Response(
            {"detail": "Cart item not found"}, status=status.HTTP_404_NOT_FOUND
        )

    cart_item.delete()
    return Response(
        {"detail": "Item removed from cart"}, status=status.HTTP_204_NO_CONTENT
    )
