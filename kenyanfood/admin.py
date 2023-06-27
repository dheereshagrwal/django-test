from django.contrib import admin
from .models import Food
 
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
#register FoodAdmin
admin.site.register(Food, FoodAdmin)