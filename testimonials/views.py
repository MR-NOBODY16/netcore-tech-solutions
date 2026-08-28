from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Testimonial


def testimonials_home(request):

    testimonials = (
        Testimonial.objects
        .filter(
            is_published=True,
        )
        .order_by(
            "display_order",
            "-featured",
            "-created_at",
        )
    )

    featured_testimonials = testimonials.filter(
        featured=True,
    )

    return render(
        request,
        "testimonials/testimonials.html",
        {
            "testimonials": testimonials,
            "featured_testimonials": featured_testimonials,
        },
    )


def testimonial_detail(
    request,
    pk,
):

    testimonial = get_object_or_404(
        Testimonial,
        pk=pk,
        is_published=True,
    )

    return render(
        request,
        "testimonials/testimonial_detail.html",
        {
            "testimonial": testimonial,
        },
    )