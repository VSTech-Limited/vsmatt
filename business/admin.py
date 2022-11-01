from django.contrib import admin

# Register your models here.
from business.models import BusinessCategory, BusinessBranch, BusinessProfile


@admin.register(BusinessCategory)
class BusinessCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'created_by', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', 'slug']
    date_hierarchy = 'created_at'
    list_editable = ['slug', 'created_by']


class BusinessBranchInline(admin.TabularInline):
    prepopulated_fields = {'slug': ('name',)}
    # formfield_overrides = {
    #     map_fields.AddressField: {
    #         'widget': map_widgets.GoogleMapsAddressWidget(attrs={'data-map-type': 'roadmap'})},
    # }
    model = BusinessBranch


@admin.register(BusinessProfile)
class BusinessProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'owner', 'address', 'geolocation', 'is_approved', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [BusinessBranchInline]
    # formfield_overrides = {
    #     map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    # }
