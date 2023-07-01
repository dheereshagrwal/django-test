from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("products/", views.get_products),
    path("products/<slug:product_slug>/", views.get_product),
]