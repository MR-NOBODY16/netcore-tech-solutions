from django.db import models


class Inquiry(models.Model):

    SERVICE_CHOICES = [

        (
            "web-development",
            "Web Development",
        ),

        (
            "software-development",
            "Software Development",
        ),

        (
            "mobile-development",
            "Mobile Application Development",
        ),

        (
            "it-support",
            "IT Support",
        ),

        (
            "networking",
            "Networking",
        ),

        (
            "business-solutions",
            "Business Solutions",
        ),

        (
            "consulting",
            "Technology Consulting",
        ),

        (
            "other",
            "Other",
        ),

    ]


    BUDGET_CHOICES = [

        (
            "under-5000",
            "Below K5,000",
        ),

        (
            "5000-10000",
            "K5,000 - K10,000",
        ),

        (
            "10000-25000",
            "K10,000 - K25,000",
        ),

        (
            "25000-50000",
            "K25,000 - K50,000",
        ),

        (
            "50000-plus",
            "Above K50,000",
        ),

        (
            "not-sure",
            "Not Sure Yet",
        ),

    ]


    STATUS_CHOICES = [

        (
            "new",
            "New",
        ),

        (
            "contacted",
            "Contacted",
        ),

        (
            "in-progress",
            "In Progress",
        ),

        (
            "completed",
            "Completed",
        ),

        (
            "archived",
            "Archived",
        ),

    ]


    name = models.CharField(
        max_length=150,
    )


    email = models.EmailField()


    phone = models.CharField(
        max_length=30,
        blank=True,
    )


    company = models.CharField(
        max_length=200,
        blank=True,
    )


    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
    )


    budget = models.CharField(
        max_length=30,
        choices=BUDGET_CHOICES,
        blank=True,
    )


    message = models.TextField()


    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="new",
    )


    admin_notes = models.TextField(
        blank=True,
    )


    created_at = models.DateTimeField(
        auto_now_add=True,
    )


    updated_at = models.DateTimeField(
        auto_now=True,
    )


    class Meta:

        ordering = [
            "-created_at",
        ]


        verbose_name = "Inquiry"

        verbose_name_plural = "Inquiries"


    def __str__(self):

        return (
            f"{self.name} - "
            f"{self.get_service_display()}"
        )