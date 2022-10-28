from django.contrib import admin

# Register your models here.
from .models import Profile


@admin.register(Profile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','gender', 'image', 'bio', 'phone_number', 'dob')
    list_filter = ('user', 'gender', 'languages')
    search_fields = ('user', 'bio', 'phone_number')
    raw_id_fields = ('user',)
    date_hierarchy = 'created_at'
