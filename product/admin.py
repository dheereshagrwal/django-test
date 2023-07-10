from django.contrib import admin
from .models import Product
import admin_thumbnails
# Register your models here.




@admin_thumbnails.thumbnail("image")
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
        "price",
        "category",
        'description',
        'avg_rating',
    )
    # description is prepopulated from name
    prepopulated_fields = {
        "slug": ("name",),
    }
    list_editable = ("price","avg_rating",)
    search_fields = ["name", "slug", "description"]



admin.site.register(Product, ProductAdmin)
