from django.contrib import admin

# Register your models here.
from business.models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'business', 'phone_number', 'message', 'is_addressed', 'created_at']
    list_filter = ['is_addressed', 'created_at','business']
    search_fields = ['name', 'email', 'phone_number', 'message']
    date_hierarchy = 'created_at'
