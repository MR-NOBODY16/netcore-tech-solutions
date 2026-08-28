from django.contrib import admin

from .models import (
    SiteSettings,
    AboutProfile,
    LeadershipProfile,
    CompanyValue,
)


# ==========================================================
# NETCORE ADMIN BRANDING
# ==========================================================

admin.site.site_header = "NetCore TECH Solutions"
admin.site.site_title = "NetCore TECH Solutions | Administration"
admin.site.index_title = "NetCore Administration"
admin.site.site_url = "/"


# ==========================================================
# SITE SETTINGS
# ==========================================================

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):

    fieldsets = (

        (
            "Company Information",
            {
                "fields": (
                    "company_name",
                    "tagline",
                ),
            },
        ),

        (
            "Homepage",
            {
                "fields": (
                    "hero_title",
                    "hero_description",
                ),
            },
        ),

        (
            "Contact Information",
            {
                "fields": (
                    "phone",
                    "email",
                    "address",
                    "whatsapp",
                ),
            },
        ),

        (
            "Social Media",
            {
                "fields": (
                    "facebook_url",
                    "linkedin_url",
                    "tiktok_url",
                    "instagram_url",
                    "youtube_url",
                ),
            },
        ),

        (
            "Footer",
            {
                "fields": (
                    "footer_description",
                ),
            },
        ),

        (
            "System",
            {
                "fields": (
                    "updated_at",
                ),
            },
        ),

    )

    readonly_fields = (
        "updated_at",
    )

    def has_add_permission(
        self,
        request,
    ):
        if SiteSettings.objects.exists():
            return False

        return super().has_add_permission(request)

    def has_delete_permission(
        self,
        request,
        obj=None,
    ):
        return False


# ==========================================================
# ABOUT PROFILE
# ==========================================================

@admin.register(AboutProfile)
class AboutProfileAdmin(admin.ModelAdmin):

    fieldsets = (

        (
            "Company Introduction",
            {
                "fields": (
                    "company_name",
                    "short_intro",
                    "founded_year",
                ),
            },
        ),

        (
            "Our Background & Story",
            {
                "fields": (
                    "our_story",
                    "why_we_started",
                    "problem_we_wanted_to_solve",
                    "how_we_started",
                    "initial_services",
                    "how_we_have_grown",
                ),
            },
        ),

        (
            "Who We Are",
            {
                "fields": (
                    "who_we_are",
                    "what_we_do",
                    "what_makes_us_different",
                ),
            },
        ),

        (
            "Mission & Vision",
            {
                "fields": (
                    "mission",
                    "vision",
                ),
            },
        ),

        (
            "Future",
            {
                "fields": (
                    "future_goals",
                ),
            },
        ),

        (
            "Publishing",
            {
                "fields": (
                    "is_active",
                    "updated_at",
                ),
            },
        ),

    )

    readonly_fields = (
        "updated_at",
    )

    list_display = (
        "company_name",
        "founded_year",
        "is_active",
        "updated_at",
    )

    list_filter = (
        "is_active",
        "founded_year",
    )

    search_fields = (
        "company_name",
        "who_we_are",
        "our_story",
    )

    def has_add_permission(
        self,
        request,
    ):
        if AboutProfile.objects.exists():
            return False

        return super().has_add_permission(request)

    def has_delete_permission(
        self,
        request,
        obj=None,
    ):
        return False


# ==========================================================
# LEADERSHIP
# ==========================================================

@admin.register(LeadershipProfile)
class LeadershipProfileAdmin(admin.ModelAdmin):

    fieldsets = (

        (
            "Personal Information",
            {
                "fields": (
                    "full_name",
                    "photo",
                ),
            },
        ),

        (
            "Professional Information",
            {
                "fields": (
                    "position",
                    "professional_title",
                    "short_bio",
                    "professional_background",
                    "education",
                    "professional_skills",
                ),
            },
        ),

        (
            "Contact & Social",
            {
                "fields": (
                    "email",
                    "linkedin_url",
                    "facebook_url",
                ),
            },
        ),

        (
            "Display",
            {
                "fields": (
                    "display_order",
                    "is_active",
                ),
            },
        ),

    )

    list_display = (
        "full_name",
        "position",
        "professional_title",
        "is_active",
        "display_order",
    )

    list_filter = (
        "is_active",
        "position",
    )

    search_fields = (
        "full_name",
        "position",
        "professional_title",
        "professional_background",
    )


# ==========================================================
# COMPANY VALUES
# ==========================================================

@admin.register(CompanyValue)
class CompanyValueAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "display_order",
        "is_active",
    )

    list_filter = (
        "is_active",
    )

    search_fields = (
        "title",
        "description",
    )

    list_editable = (
        "display_order",
        "is_active",
    )