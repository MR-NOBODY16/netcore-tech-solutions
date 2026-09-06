from django.shortcuts import render

from blog.models import Post
from portfolio.models import PortfolioProject
from services.models import Service

from .models import (
    AboutProfile,
    CompanyValue,
    LeadershipProfile,
)


# ==========================================================
# HOME
# ==========================================================

def home(request):
    """
    Main NetCore TECH Solutions homepage.

    The homepage pulls live published content from the
    Services, Portfolio and Blog applications.
    """

    featured_services = (
        Service.objects
        .filter(
            is_published=True,
            featured=True,
        )
        .order_by(
            "order",
            "-created_at",
        )[:6]
    )

    featured_projects = (
        PortfolioProject.objects
        .filter(
            is_published=True,
            is_featured=True,
        )
        .order_by(
            "-created_at",
        )[:3]
    )

    latest_posts = (
        Post.objects
        .filter(
            is_published=True,
        )
        .order_by(
            "-featured",
            "-published_at",
            "-created_at",
        )[:3]
    )

    context = {
        "featured_services": featured_services,
        "featured_projects": featured_projects,
        "latest_posts": latest_posts,

        "published_service_count": (
            Service.objects
            .filter(is_published=True)
            .count()
        ),

        "published_project_count": (
            PortfolioProject.objects
            .filter(is_published=True)
            .count()
        ),

        "published_post_count": (
            Post.objects
            .filter(is_published=True)
            .count()
        ),
    }

    return render(
        request,
        "core/home.html",
        context,
    )


# ==========================================================
# ABOUT
# ==========================================================

def about(request):
    about_profile = (
        AboutProfile.objects
        .filter(
            is_active=True,
        )
        .first()
    )

    leadership = (
        LeadershipProfile.objects
        .filter(
            is_active=True,
        )
        .order_by(
            "display_order",
            "full_name",
        )
    )

    company_values = (
        CompanyValue.objects
        .filter(
            is_active=True,
        )
        .order_by(
            "display_order",
            "title",
        )
    )

    context = {
        "about_profile": about_profile,
        "leadership": leadership,
        "company_values": company_values,
    }

    return render(
        request,
        "core/about.html",
        context,
    )


# ==========================================================
# SERVICES
# ==========================================================

def services(request):
    return render(
        request,
        "core/services.html",
    )


# ==========================================================
# PRIVACY POLICY
# ==========================================================

def privacy(request):
    return render(
        request,
        "core/privacy.html",
    )


# ==========================================================
# TERMS OF SERVICE
# ==========================================================

def terms(request):
    return render(
        request,
        "core/terms.html",
    )