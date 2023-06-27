from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path("categories/", views.get_categories),
    path("categories/<slug:category_slug>/", views.get_category),
]