from django.contrib import admin

from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "service",
        "budget",
        "status",
        "created_at",
    )

    list_filter = (
        "service",
        "budget",
        "status",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "company",
        "message",
    )

    list_editable = (
        "status",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (

        (
            "Customer Information",
            {
                "fields": (
                    "name",
                    "email",
                    "phone",
                    "company",
                ),
            },
        ),

        (
            "Project Information",
            {
                "fields": (
                    "service",
                    "budget",
                    "message",
                ),
            },
        ),

        (
            "Inquiry Management",
            {
                "fields": (
                    "status",
                    "admin_notes",
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
        "-created_at",
    )