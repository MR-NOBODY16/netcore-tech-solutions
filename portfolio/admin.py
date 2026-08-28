from django.contrib import admin

from .models import (
    PortfolioProject,
    ProjectScreenshot,
    ProjectTechnology,
)


# ==========================================================
# PROJECT SCREENSHOT INLINE
# ==========================================================

class ProjectScreenshotInline(admin.TabularInline):

    model = ProjectScreenshot

    extra = 1

    fields = (
        "image",
        "title",
        "description",
        "display_order",
    )

    ordering = (
        "display_order",
        "created_at",
    )


# ==========================================================
# PORTFOLIO PROJECT ADMIN
# ==========================================================

@admin.register(PortfolioProject)
class PortfolioProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "client",
        "year",
        "status",
        "is_featured",
        "is_published",
        "created_at",
    )

    list_filter = (
        "category",
        "status",
        "is_featured",
        "is_published",
        "year",
    )

    search_fields = (
        "title",
        "slug",
        "client",
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

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    list_editable = (
        "is_featured",
        "is_published",
    )

    ordering = (
        "-is_featured",
        "-created_at",
    )

    date_hierarchy = "created_at"

    inlines = [
        ProjectScreenshotInline,
    ]

    fieldsets = (

        (
            "Project Information",
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
            "Project Details",
            {
                "fields": (
                    "client",
                    "year",
                    "status",
                    "featured_image",
                ),
            },
        ),

        (
            "Case Study",
            {
                "fields": (
                    "challenge",
                    "solution",
                    "results",
                ),
                "classes": (
                    "collapse",
                ),
            },
        ),

        (
            "Technologies & Features",
            {
                "fields": (
                    "technologies",
                    "features",
                ),
                "description": (
                    "Enter technologies and features separated "
                    "by commas."
                ),
            },
        ),

        (
            "Project Links",
            {
                "fields": (
                    "live_url",
                    "github_url",
                ),
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "is_featured",
                    "is_published",
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


# ==========================================================
# PROJECT TECHNOLOGY ADMIN
# ==========================================================

@admin.register(ProjectTechnology)
class ProjectTechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
        "icon",
        "created_at",
    )

    search_fields = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": (
            "name",
        ),
    }

    readonly_fields = (
        "created_at",
    )

    ordering = (
        "name",
    )


# ==========================================================
# PROJECT SCREENSHOT ADMIN
# ==========================================================

@admin.register(ProjectScreenshot)
class ProjectScreenshotAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "title",
        "display_order",
        "created_at",
    )

    list_filter = (
        "project",
    )

    search_fields = (
        "project__title",
        "title",
        "description",
    )

    ordering = (
        "project",
        "display_order",
    )

    readonly_fields = (
        "created_at",
    )