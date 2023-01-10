from django.contrib import admin 
from .forms import CustomUserChangeForm , CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
# Register your models here.
# admin.site.register(CustomUser)

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = CustomUserCreationForm
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('first_name','last_name','avatar','location','gender','age')}),
    )
    form = CustomUserChangeForm
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('avatar','location','gender','age')}),
    )

admin.site.register(CustomUser,CustomUserAdmin)