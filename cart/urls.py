from django.urls import path
from . import views

urlpatterns = [
    path('cart/<str:cart_id>', views.get_cart, name='get_cart'),
    path('cart/create/<str:cart_id>', views.create_cart, name='create_cart'),
    path('cart/clear/<str:cart_id>', views.clear_cart, name='clear_cart'),

    path('cart/items/<str:cart_id>', views.get_cart_items, name='get_cart_items'),
    path('cart/items/add/<str:cart_id>/<str:product_slug>', views.add_cart_item, name='add_to_cart'),
    path('cart/items/update/<str:cart_id>/<str:product_slug>', views.update_cart_item, name='update_cart_item'),
    path('cart/items/remove/<str:cart_id>/<str:product_slug>', views.remove_cart_item, name='remove_from_cart'),
]
