from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Service


def services_home(request):

    services = (
        Service.objects
        .filter(
            is_published=True,
        )
        .order_by(
            "order",
            "-featured",
            "-created_at",
        )
    )

    featured_services = services.filter(
        featured=True,
    )

    return render(
        request,
        "services/services.html",
        {
            "services": services,
            "featured_services": featured_services,
        },
    )


def service_detail(
    request,
    slug,
):

    service = get_object_or_404(
        Service,
        slug=slug,
        is_published=True,
    )

    related_services = (
        Service.objects
        .filter(
            is_published=True,
            category=service.category,
        )
        .exclude(
            pk=service.pk,
        )
        .order_by(
            "order",
            "-created_at",
        )[:3]
    )

    return render(
        request,
        "services/service_detail.html",
        {
            "service": service,
            "related_services": related_services,
        },
    )