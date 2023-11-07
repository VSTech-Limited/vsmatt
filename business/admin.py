from django.contrib import admin

# Register your models here.
from business.models import BusinessCategory, BusinessBranch, BusinessProfile, BranchReview

class BusinessBranchInline(admin.TabularInline):
    prepopulated_fields = {'slug': ('name',)}
    model = BusinessBranch
    extra = 0
    readonly_fields = ['business', 'customer_service_number', 'longitude', 'latitude', 'address', 'image']
    exclude = ['description', 'additional_info']

@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_by', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'slug']
    date_hierarchy = 'created_at'
    inlines = [BusinessBranchInline]

@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'owner', 'address', 'geolocation', 'is_approved', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BusinessBranchInline]

@admin.register(BranchReview)
class BranchReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'business', 'rating', 'created', 'updated', 'review']
    list_filter = ['user', 'created', 'updated', 'rating', 'business']
