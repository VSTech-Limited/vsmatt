from django.contrib import admin

# Register your models here.
from .models import ProductCategory, Product, ProductSecondaryImages, ProductReview


@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_by', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'slug']
    date_hierarchy = 'created_at'
    list_editable = ['slug', 'created_by']


class ProductSecondaryImagesInline(admin.TabularInline):
    model = ProductSecondaryImages
    raw_id_fields = ['product']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated', 'rating']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductSecondaryImagesInline]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'created', 'updated', 'review']
    list_filter = ['user', 'created', 'updated', 'rating', 'product']
    list_editable = ['rating', 'product']
