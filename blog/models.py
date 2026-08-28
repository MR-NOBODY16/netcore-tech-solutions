from django.db import models

from django.urls import reverse


class Post(models.Model):

    CATEGORY_CHOICES = [

        (
            "technology",
            "Technology",
        ),

        (
            "web",
            "Web Development",
        ),

        (
            "software",
            "Software Development",
        ),

        (
            "networking",
            "Networking",
        ),

        (
            "it-support",
            "IT Support",
        ),

        (
            "business",
            "Business Technology",
        ),

        (
            "news",
            "Company News",
        ),

        (
            "tutorial",
            "Tutorial",
        ),

    ]


    title = models.CharField(
        max_length=250,
    )


    slug = models.SlugField(
        max_length=280,
        unique=True,
    )


    excerpt = models.TextField(
        max_length=500,
    )


    content = models.TextField()


    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES,
    )


    featured_image = models.ImageField(
        upload_to="blog/",
        blank=True,
        null=True,
    )


    author = models.CharField(
        max_length=150,
        default="NetCore TECH Solutions",
    )


    featured = models.BooleanField(
        default=False,
    )


    is_published = models.BooleanField(
        default=True,
    )


    published_at = models.DateTimeField(
        blank=True,
        null=True,
    )


    created_at = models.DateTimeField(
        auto_now_add=True,
    )


    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        ordering = [
            "-featured",
            "-published_at",
            "-created_at",
        ]


        verbose_name = "Blog Post"

        verbose_name_plural = "Blog Posts"


    def __str__(self):

        return self.title


    def get_absolute_url(self):

        return reverse(
            "blog:detail",
            kwargs={
                "slug": self.slug,
            },
        )