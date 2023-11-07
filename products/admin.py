from django.contrib import admin

# Register your models here.
from .models import ProductCategory, Product, ProductSecondaryImages, ProductReview

class ProductsInline(admin.TabularInline):
    model = Product
    readonly_fields = ['name','slug', 'price', 'available', 'branch', 'image', 'tags']
    can_delete = False
    exclude = ['description', ]
    extra = 0

@admin.register(ProductCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_by', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'slug']
    date_hierarchy = 'created_at'
    inlines = [ProductsInline]

class ProductSecondaryImagesInline(admin.StackedInline):
    model = ProductSecondaryImages
    extra = 1

class ReviewsInline(admin.TabularInline):
    model = ProductReview
    readonly_fields = ['user','rating', 'review']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProductSecondaryImagesInline, ReviewsInline]


@admin.register(ProductReview)
class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'created', 'updated', 'review']
    list_filter = ['user', 'created', 'updated', 'rating', 'product']
