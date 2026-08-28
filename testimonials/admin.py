from django.contrib import admin
from django.utils.html import format_html

from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):

    list_display = (
        "client_photo_preview",
        "client_name",
        "company",
        "position",
        "rating_display",
        "service",
        "featured",
        "is_published",
        "display_order",
        "created_at",
    )

    list_filter = (
        "rating",
        "featured",
        "is_published",
        "service",
        "created_at",
    )

    search_fields = (
        "client_name",
        "company",
        "position",
        "testimonial",
        "service",
    )

    list_editable = (
        "featured",
        "is_published",
        "display_order",
    )

    readonly_fields = (
        "client_photo_preview",
        "created_at",
        "updated_at",
    )

    ordering = (
        "display_order",
        "-featured",
        "-created_at",
    )

    date_hierarchy = "created_at"

    fieldsets = (

        (
            "Client Information",
            {
                "fields": (
                    "client_name",
                    "company",
                    "position",
                    "photo",
                    "client_photo_preview",
                ),
            },
        ),

        (
            "Testimonial",
            {
                "fields": (
                    "testimonial",
                    "rating",
                    "service",
                ),
                "description": (
                    "Enter the customer's feedback and "
                    "the service they received from NetCore."
                ),
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "featured",
                    "is_published",
                    "display_order",
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
                "classes": (
                    "collapse",
                ),
            },
        ),
    )

    def client_photo_preview(self, obj):

        if not obj.photo:
            return "No photo"

        return format_html(
            '<img src="{}" width="60" height="60" '
            'style="object-fit: cover; border-radius: 50%; '
            'border: 2px solid #087BFF;" />',
            obj.photo.url,
        )

    client_photo_preview.short_description = "Photo"

    def rating_display(self, obj):

        stars = "★" * obj.rating

        return format_html(
            '<span style="color: #087BFF; '
            'font-size: 16px;">{}</span>',
            stars,
        )

    rating_display.short_description = "Rating"