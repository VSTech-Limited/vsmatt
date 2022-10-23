from django.contrib import admin

# Register your models here.
from shop.models import ProductSecondaryImages, Product, Review, BusinessProfile, BusinessBranch

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


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'created', 'updated', 'review']
    list_filter = ['user', 'created', 'updated', 'rating', 'product']
    list_editable = ['rating', 'product']


class BusinessBranchInline(admin.TabularInline):
    prepopulated_fields = {'slug': ('name',)}
    # formfield_overrides = {
    #     map_fields.AddressField: {
    #         'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    # }
    model = BusinessBranch


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'owner', 'address', 'geolocation']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BusinessBranchInline]
    # formfield_overrides = {
    #     map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    # }
