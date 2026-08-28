from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "author",
        "featured",
        "is_published",
        "published_at",
        "created_at",
    )

    list_filter = (
        "category",
        "featured",
        "is_published",
        "published_at",
    )

    search_fields = (
        "title",
        "excerpt",
        "content",
        "author",
    )

    prepopulated_fields = {
        "slug": (
            "title",
        ),
    }

    list_editable = (
        "featured",
        "is_published",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    date_hierarchy = "published_at"

    ordering = (
        "-featured",
        "-published_at",
        "-created_at",
    )