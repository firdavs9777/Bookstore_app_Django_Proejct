from users_list.models import CustomUser
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomerUserCreationForm,CustomUserChangeForm

CustomUser = get_user_model()

# Register your form models here.
class CustomerUserAdmin(UserAdmin):
    add_form = CustomerUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username',]
admin.site.register(CustomUser,CustomerUserAdmin)