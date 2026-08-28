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

    The homepage pulls published content dynamically from
    the existing Services, Portfolio and Blog applications.

    Featured services and featured projects are controlled
    from the Django admin panel.
    """

    # ------------------------------------------------------
    # FEATURED SERVICES
    # ------------------------------------------------------
    featured_services = (
        Service.objects
        .filter(
            is_published=True,
            featured=True,
        )
        .order_by(
            "order",
            "-created_at",
        )
    )

    # ------------------------------------------------------
    # FEATURED PORTFOLIO PROJECTS
    # ------------------------------------------------------
    featured_projects = (
        PortfolioProject.objects
        .filter(
            is_published=True,
            is_featured=True,
        )
        .order_by(
            "-created_at",
        )
    )

    # ------------------------------------------------------
    # LATEST BLOG POSTS
    # ------------------------------------------------------
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

    # ------------------------------------------------------
    # HOMEPAGE CONTEXT
    # ------------------------------------------------------
    context = {
        "featured_services": featured_services,
        "featured_projects": featured_projects,
        "latest_posts": latest_posts,
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
    """
    About page.

    Content is managed dynamically through the Django admin.
    """

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
    """
    Services landing page.
    """

    return render(
        request,
        "core/services.html",
    )


# ==========================================================
# PRIVACY POLICY
# ==========================================================

def privacy(request):
    """
    Privacy policy page.
    """

    return render(
        request,
        "core/privacy.html",
    )


# ==========================================================
# TERMS OF SERVICE
# ==========================================================

def terms(request):
    """
    Terms of service page.
    """

    return render(
        request,
        "core/terms.html",
    )