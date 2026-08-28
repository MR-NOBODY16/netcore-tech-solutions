from django.db import models
from django.urls import reverse


class Testimonial(models.Model):

    RATING_CHOICES = [
        (5, "5 Stars"),
        (4, "4 Stars"),
        (3, "3 Stars"),
        (2, "2 Stars"),
        (1, "1 Star"),
    ]

    client_name = models.CharField(
        max_length=150,
        help_text="Full name of the client.",
    )

    company = models.CharField(
        max_length=200,
        blank=True,
        help_text="Company or organization name.",
    )

    position = models.CharField(
        max_length=150,
        blank=True,
        help_text="Client's position or professional title.",
    )

    photo = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True,
        help_text="Optional client profile photo.",
    )

    testimonial = models.TextField(
        help_text="The client's testimonial.",
    )

    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=5,
    )

    service = models.CharField(
        max_length=200,
        blank=True,
        help_text="Service the client received.",
    )

    featured = models.BooleanField(
        default=False,
        help_text="Display this testimonial prominently.",
    )

    is_published = models.BooleanField(
        default=True,
        help_text="Make this testimonial visible on the website.",
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Lower numbers appear first.",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:

        ordering = [
            "display_order",
            "-featured",
            "-created_at",
        ]

        verbose_name = "Testimonial"

        verbose_name_plural = "Testimonials"

    def __str__(self):

        return self.client_name

    def get_absolute_url(self):

        return reverse(
            "testimonials:detail",
            kwargs={
                "pk": self.pk,
            },
        )