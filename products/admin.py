from django.contrib import admin

# Register your models here.
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'image','price', 'created_at')
    search_fields = ('name', 'category')
    list_filter = ('category',)

admin.site.register(Product, ProductAdmin)