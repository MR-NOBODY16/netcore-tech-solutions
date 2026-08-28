from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "featured",
        "is_published",
        "order",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "is_published",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
        "technologies",
        "features",
    )

    prepopulated_fields = {
        "slug": (
            "title",
        ),
    }

    list_editable = (
        "featured",
        "is_published",
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Basic Information",
            {
                "fields": (
                    "title",
                    "slug",
                    "category",
                    "short_description",
                    "description",
                ),
            },
        ),

        (
            "Visual",
            {
                "fields": (
                    "icon",
                    "image",
                ),
            },
        ),

        (
            "Technology",
            {
                "fields": (
                    "technologies",
                ),
            },
        ),

        (
            "Service Features",
            {
                "fields": (
                    "features",
                ),
                "description": (
                    "Enter each feature on a separate line."
                ),
            },
        ),

        (
            "Our Process",
            {
                "fields": (
                    "process",
                ),
                "description": (
                    "Enter each process step on a separate line."
                ),
            },
        ),

        (
            "Pricing",
            {
                "fields": (
                    "price_from",
                ),
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "featured",
                    "is_published",
                    "order",
                ),
            },
        ),

        (
            "System Information",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
            },
        ),

    )

    ordering = (
        "order",
        "-featured",
        "-created_at",
    )