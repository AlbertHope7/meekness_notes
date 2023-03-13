from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class AccountAdmin(admin.ModelAdmin):
    list_display = ["email", "username", "date_joined"]
