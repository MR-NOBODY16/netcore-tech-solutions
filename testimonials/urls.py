from django.urls import path

from . import views


app_name = "testimonials"


urlpatterns = [

    path(
        "",
        views.testimonials_home,
        name="home",
    ),

    path(
        "<int:pk>/",
        views.testimonial_detail,
        name="detail",
    ),
]