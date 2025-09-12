from django.contrib import admin
from .models import Book

from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

class BookAdmin(admin.ModelAdmin):
    list_filter = ('title', 'author',)
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)



class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("username", "email", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "date_of_birth")
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "date_of_birth", "profile_photo", "is_staff", "is_active"),
        }),
    )
    search_fields = ("username", "email")
    ordering = ("username",)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date')  
    list_filter = ('author', 'publication_date')  

admin.site.register(CustomUser, CustomUserAdmin)