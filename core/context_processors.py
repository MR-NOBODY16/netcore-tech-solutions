from .models import SiteSettings

from portfolio.models import PortfolioProject
from services.models import Service
from blog.models import Post
from inquiries.models import Inquiry


def site_settings(request):

    settings = SiteSettings.objects.first()

    return {
        "site_settings": settings,
    }


def netcore_admin_stats(request):

    # Only calculate these statistics for Django Admin pages.
    if not request.path.startswith("/admin/"):
        return {
            "netcore_stats": {
                "projects": 0,
                "services": 0,
                "posts": 0,
                "inquiries": 0,
                "new_inquiries": 0,
            },
        }

    projects = PortfolioProject.objects.count()

    services = Service.objects.filter(
        is_published=True,
    ).count()

    posts = Post.objects.filter(
        is_published=True,
    ).count()

    inquiries = Inquiry.objects.count()

    new_inquiries = Inquiry.objects.filter(
        status="new",
    ).count()

    return {
        "netcore_stats": {
            "projects": projects,
            "services": services,
            "posts": posts,
            "inquiries": inquiries,
            "new_inquiries": new_inquiries,
        },
    }