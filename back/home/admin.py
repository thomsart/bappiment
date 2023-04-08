from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Status, Membership
from .forms import CustomUserCreationForm, CustomUserChangeForm



class CustomUserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('email', 'first_name', 'last_name', 'is_staff')
    fieldsets = (
        ('Logs', {'fields': ('email', 'password')}),
        ('User', {'fields': (
                    'first_name', 'last_name', 'phone', 'days_off', 
                    'days_off_cumul', 'hightest_level', 'permanent_contract'
                    )
                }
        ),
        ('Permission', {'fields': ('is_staff', 'is_active', 'groups')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        })
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('first_name', 'last_name')


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Membership)