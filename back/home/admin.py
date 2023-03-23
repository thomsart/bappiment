from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Status
from .forms import CustomUserCreationForm, CustomUserChangeForm



class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'is_staff')
    list_filter = ('email', 'is_staff')
    fieldsets = (
        ('Logs', {'fields': ('email', 'password')}),
        ('User', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permission', {'fields': ('is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        })
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)