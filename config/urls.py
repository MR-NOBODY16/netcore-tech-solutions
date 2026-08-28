from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path


urlpatterns = [

    path(
        "admin/",
        admin.site.urls,
    ),

    path(
        "",
        include("core.urls"),
    ),

    path(
        "services/",
        include("services.urls"),
    ),

    path(
        "portfolio/",
        include("portfolio.urls"),
    ),

    path(
        "blog/",
        include("blog.urls"),
    ),
 
    path(
        "testimonials/",
        include("testimonials.urls"),
    ),
    
    path(
        "contact/",
        include("inquiries.urls"),
    ),

]


if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )