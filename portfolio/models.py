from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PortfolioProject(models.Model):
    """
    Main portfolio project model.

    Each project represents a real project developed,
    maintained, or showcased by NetCore.
    """

    CATEGORY_CHOICES = [
        ("web", "Web Development"),
        ("software", "Software Development"),
        ("mobile", "Mobile Application"),
        ("networking", "Networking"),
        ("it-support", "IT Support"),
        ("education", "Education Technology"),
        ("business", "Business Solution"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("ongoing", "Ongoing"),
        ("maintenance", "Maintenance"),
        ("concept", "Concept"),
    ]

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=220,
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
        default="web"
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    client = models.CharField(
        max_length=200,
        blank=True
    )

    year = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="completed"
    )

    featured_image = models.ImageField(
        upload_to="portfolio/projects/",
        blank=True,
        null=True
    )

    challenge = models.TextField(
        blank=True
    )

    solution = models.TextField(
        blank=True
    )

    results = models.TextField(
        blank=True
    )

    technologies = models.TextField(
        blank=True,
        help_text=(
            "Enter technologies separated by commas. "
            "Example: Django, Python, Tailwind CSS, SQLite"
        )
    )

    features = models.TextField(
        blank=True,
        help_text=(
            "Enter major features separated by commas."
        )
    )

    live_url = models.URLField(
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    is_featured = models.BooleanField(
        default=False
    )

    is_published = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = [
            "-is_featured",
            "-created_at",
        ]

        verbose_name = "Portfolio Project"

        verbose_name_plural = "Portfolio Projects"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        """
        Automatically generate a URL-friendly slug
        when one hasn't been provided.
        """

        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            counter = 1

            while PortfolioProject.objects.filter(
                slug=slug
            ).exclude(pk=self.pk).exists():

                slug = f"{base_slug}-{counter}"

                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "portfolio:detail",
            kwargs={
                "slug": self.slug
            }
        )

    def get_technologies(self):
        """
        Convert the comma-separated technology field
        into a clean list.
        """

        if not self.technologies:
            return []

        return [
            technology.strip()
            for technology in self.technologies.split(",")
            if technology.strip()
        ]

    def get_features(self):
        """
        Convert the comma-separated features field
        into a clean list.
        """

        if not self.features:
            return []

        return [
            feature.strip()
            for feature in self.features.split(",")
            if feature.strip()
        ]


class ProjectScreenshot(models.Model):
    """
    Stores multiple screenshots for a portfolio project.
    """

    project = models.ForeignKey(
        PortfolioProject,
        on_delete=models.CASCADE,
        related_name="screenshots"
    )

    image = models.ImageField(
        upload_to="portfolio/screenshots/"
    )

    title = models.CharField(
        max_length=200,
        blank=True
    )

    description = models.CharField(
        max_length=300,
        blank=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = [
            "display_order",
            "created_at",
        ]

        verbose_name = "Project Screenshot"

        verbose_name_plural = "Project Screenshots"

    def __str__(self):

        if self.title:
            return f"{self.project.title} — {self.title}"

        return f"{self.project.title} — Screenshot"


class ProjectTechnology(models.Model):
    """
    Optional structured technology model.

    This allows us to eventually move away from
    comma-separated technology names if the portfolio
    becomes larger.
    """

    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=120,
        unique=True,
        blank=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional icon identifier."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]

        verbose_name = "Project Technology"

        verbose_name_plural = "Project Technologies"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)