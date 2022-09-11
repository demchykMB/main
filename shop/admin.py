from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategyAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'uploaded', 'image']
    list_filter = ['available', 'created', 'created']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name', )}