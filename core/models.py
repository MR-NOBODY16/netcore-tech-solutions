from django.db import models
from django.core.validators import MinValueValidator


class SiteSettings(models.Model):

    company_name = models.CharField(
        max_length=200,
        default="NetCore TECH Solutions",
    )

    tagline = models.CharField(
        max_length=255,
        default="Connecting technology, empowering businesses.",
    )

    hero_title = models.CharField(
        max_length=255,
        default="Technology that moves your business forward.",
    )

    hero_description = models.TextField(
        default=(
            "We build practical digital solutions that help "
            "businesses work smarter, operate efficiently and grow."
        ),
    )

    phone = models.CharField(
        max_length=50,
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    address = models.TextField(
        blank=True,
    )

    whatsapp = models.CharField(
        max_length=50,
        blank=True,
    )

    facebook_url = models.URLField(
        blank=True,
    )

    linkedin_url = models.URLField(
        blank=True,
    )

    tiktok_url = models.URLField(
        blank=True,
    )

    instagram_url = models.URLField(
        blank=True,
    )

    youtube_url = models.URLField(
        blank=True,
    )

    footer_description = models.TextField(
        default=(
            "Connecting technology, empowering businesses. "
            "We build practical digital solutions for modern organizations."
        ),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return self.company_name


# ==========================================================
# ABOUT PROFILE
# ==========================================================

class AboutProfile(models.Model):

    company_name = models.CharField(
        max_length=200,
        default="NetCore TECH Solutions",
    )

    short_intro = models.TextField(
        default=(
            "NetCore TECH Solutions is a technology-focused company "
            "providing practical digital and IT solutions for modern "
            "businesses and organizations."
        ),
    )

    # ------------------------------------------------------
    # COMPANY BACKGROUND
    # ------------------------------------------------------

    founded_year = models.PositiveIntegerField(
        blank=True,
        null=True,
        validators=[
            MinValueValidator(1900),
        ],
    )

    our_story = models.TextField(
        blank=True,
        help_text="The main story and background of the company.",
    )

    why_we_started = models.TextField(
        blank=True,
        help_text="Why NetCore was created.",
    )

    problem_we_wanted_to_solve = models.TextField(
        blank=True,
        help_text="The problem or gap NetCore wanted to address.",
    )

    how_we_started = models.TextField(
        blank=True,
        help_text="Describe how NetCore started.",
    )

    initial_services = models.TextField(
        blank=True,
        help_text="Services NetCore initially offered.",
    )

    how_we_have_grown = models.TextField(
        blank=True,
        help_text="Describe the growth and development of NetCore.",
    )

    # ------------------------------------------------------
    # COMPANY PROFILE
    # ------------------------------------------------------

    who_we_are = models.TextField(
        blank=True,
        help_text="Professional description of who NetCore is.",
    )

    what_we_do = models.TextField(
        blank=True,
        help_text="Describe what NetCore does.",
    )

    what_makes_us_different = models.TextField(
        blank=True,
        help_text="What makes NetCore different from other companies.",
    )

    future_goals = models.TextField(
        blank=True,
        help_text="Where NetCore wants to go in the future.",
    )

    # ------------------------------------------------------
    # MISSION & VISION
    # ------------------------------------------------------

    mission = models.TextField(
        blank=True,
    )

    vision = models.TextField(
        blank=True,
    )

    # ------------------------------------------------------
    # DISPLAY
    # ------------------------------------------------------

    is_active = models.BooleanField(
        default=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "About Profile"
        verbose_name_plural = "About Profile"

    def __str__(self):
        return self.company_name


# ==========================================================
# LEADERSHIP / PROFESSIONAL PROFILE
# ==========================================================

class LeadershipProfile(models.Model):

    full_name = models.CharField(
        max_length=200,
    )

    position = models.CharField(
        max_length=200,
        help_text="Example: Founder & Managing Director",
    )

    professional_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Example: IT Specialist, Software Developer",
    )

    photo = models.ImageField(
        upload_to="leadership/",
        blank=True,
        null=True,
    )

    short_bio = models.TextField(
        blank=True,
        help_text="Short professional biography.",
    )

    professional_background = models.TextField(
        blank=True,
        help_text="Professional background and experience.",
    )

    education = models.TextField(
        blank=True,
        help_text="Relevant educational background.",
    )

    professional_skills = models.TextField(
        blank=True,
        help_text="Professional skills and areas of expertise.",
    )

    linkedin_url = models.URLField(
        blank=True,
    )

    facebook_url = models.URLField(
        blank=True,
    )

    email = models.EmailField(
        blank=True,
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        verbose_name = "Leadership Profile"
        verbose_name_plural = "Leadership Profiles"
        ordering = [
            "display_order",
            "full_name",
        ]

    def __str__(self):
        return f"{self.full_name} — {self.position}"


# ==========================================================
# COMPANY VALUES
# ==========================================================

class CompanyValue(models.Model):

    title = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    icon = models.CharField(
        max_length=50,
        blank=True,
        help_text="Optional icon name or symbol.",
    )

    display_order = models.PositiveIntegerField(
        default=0,
    )

    is_active = models.BooleanField(
        default=True,
    )

    class Meta:
        verbose_name = "Company Value"
        verbose_name_plural = "Company Values"
        ordering = [
            "display_order",
            "title",
        ]

    def __str__(self):
        return self.title
    
    

class Testimonial(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(
        max_length=150,
        blank=True,
        help_text="Example: Business Owner, School Administrator, Client"
    )
    company = models.CharField(
        max_length=150,
        blank=True
    )
    message = models.TextField()
    photo = models.ImageField(
        upload_to="testimonials/",
        blank=True,
        null=True
    )

    rating = models.PositiveSmallIntegerField(
        default=5,
        choices=[
            (1, "1 Star"),
            (2, "2 Stars"),
            (3, "3 Stars"),
            (4, "4 Stars"),
            (5, "5 Stars"),
        ]
    )

    is_featured = models.BooleanField(
        default=True,
        help_text="Show this testimonial on the homepage."
    )

    is_active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return self.name