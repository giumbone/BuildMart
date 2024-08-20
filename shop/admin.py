from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at')
    list_editable = ('price', 'stock')
    search_fields = ('name', 'price')
    list_filter = ('price', 'stock')
    date_hierarchy = 'created_at' 
    prepopulated_fields = {"slug": ("name",)}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)