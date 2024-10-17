from django.contrib import admin
from .models import *

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name']
    list_display_links = ['id']

admin.site.register(Person, PersonAdmin)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'password', 'email']
    list_display_links = ['id']

admin.site.register(CustomUser, CustomUserAdmin)
