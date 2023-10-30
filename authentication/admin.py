from django.contrib import admin

from authentication.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'phone',
        'birth_date',
        'is_staff',
        'is_superuser',
        'is_active',
        'last_login',
        'image'
    ]
    search_fields = ['phone', 'birth_date', 'last_login']
    list_filter = ['is_active', 'is_superuser']

