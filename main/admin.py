from django.contrib import admin
from main.models import Category, Condition, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category_name',
    )
    search_fields = (
        'category_name',
    )

@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'condition_name',
    )
    search_fields = (
        'condition_name',
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'product_category_name',
        'product_price',
        'product_condition',
        'product_minimum_order',
        'product_description',
        'product_created_date',
    )
    list_filter = (
        'product_category_name',
        'product_condition',
    )
    search_fields = (
        'product_name',
    )
    list_per_page = 15