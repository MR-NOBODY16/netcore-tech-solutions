from django.shortcuts import get_object_or_404, render

from .models import PortfolioProject


def home(request):
    """
    Portfolio landing page.
    """

    projects = (
        PortfolioProject.objects
        .filter(is_published=True)
        .order_by(
            "-is_featured",
            "-created_at",
        )
    )

    featured_projects = (
        PortfolioProject.objects
        .filter(
            is_published=True,
            is_featured=True,
        )
        .order_by("-created_at")
    )

    context = {
        "projects": projects,
        "featured_projects": featured_projects,
    }

    return render(
        request,
        "portfolio/home.html",
        context,
    )


def detail(request, slug):
    """
    Individual project case-study page.
    """

    project = get_object_or_404(
        PortfolioProject,
        slug=slug,
        is_published=True,
    )

    related_projects = (
        PortfolioProject.objects
        .filter(
            is_published=True,
            category=project.category,
        )
        .exclude(
            pk=project.pk,
        )
        .order_by(
            "-is_featured",
            "-created_at",
        )[:3]
    )

    context = {
        "project": project,
        "related_projects": related_projects,
    }

    return render(
        request,
        "portfolio/detail.html",
        context,
    )