from django.db import models
from django.urls import reverse


class Service(models.Model):

    CATEGORY_CHOICES = [

        (
            "digital",
            "Digital Solutions",
        ),

        (
            "software",
            "Software Development",
        ),

        (
            "infrastructure",
            "IT & Infrastructure",
        ),

        (
            "consulting",
            "Technology Consulting",
        ),

    ]

    title = models.CharField(
        max_length=200,
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
    )

    short_description = models.TextField(
        max_length=400,
        help_text=(
            "Short description displayed on the services page."
        ),
    )

    description = models.TextField(
        help_text=(
            "Full description of the service."
        ),
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="digital",
    )

    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text=(
            "Optional icon name or identifier."
        ),
    )

    image = models.ImageField(
        upload_to="services/",
        blank=True,
        null=True,
    )

    technologies = models.CharField(
        max_length=500,
        blank=True,
        help_text=(
            "Separate technologies with commas."
        ),
    )

    features = models.TextField(
        blank=True,
        help_text=(
            "Enter one feature per line."
        ),
    )

    process = models.TextField(
        blank=True,
        help_text=(
            "Enter one process step per line."
        ),
    )

    price_from = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        blank=True,
        null=True,
        help_text=(
            "Optional starting price in Zambian Kwacha."
        ),
    )

    featured = models.BooleanField(
        default=False,
    )

    is_published = models.BooleanField(
        default=True,
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text=(
            "Lower numbers appear first."
        ),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        ordering = [
            "order",
            "-featured",
            "-created_at",
        ]

        verbose_name = "Service"

        verbose_name_plural = "Services"


    def __str__(self):

        return self.title


    def get_absolute_url(self):

        return reverse(
            "services:detail",
            kwargs={
                "slug": self.slug,
            },
        )


    def get_features(self):

        return [
            item.strip()
            for item in self.features.splitlines()
            if item.strip()
        ]


    def get_process_steps(self):

        return [
            item.strip()
            for item in self.process.splitlines()
            if item.strip()
        ]


    def get_technologies(self):

        return [
            item.strip()
            for item in self.technologies.split(",")
            if item.strip()
        ]