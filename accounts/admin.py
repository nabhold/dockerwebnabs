from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()


class ProfileInline(admin.StackedInline):
    """
    Inline admin descriptor for Profile model.
    """

    model = Profile
    can_delete = False
    verbose_name_plural = "Profiles"


@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    """
    Admin interface for CustomUser model.
    """

    inlines = (ProfileInline,)

    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
    )
    list_filter = ("is_staff", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "date_of_birth",
                    "phone_number",
                    "address",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "date_of_birth",
                    "phone_number",
                    "address",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("email",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for Profile model.
    """

    model = Profile
    list_display = ("user", "date_of_birth", "phone_number", "website")
    list_filter = ("date_of_birth",)
    search_fields = ("user__email", "user__username", "date_of_birth")
