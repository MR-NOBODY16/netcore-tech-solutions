from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.shortcuts import render

from .models import Inquiry


# ==========================================================
# CONTACT / INQUIRY
# ==========================================================

def contact(request):

    # ======================================================
    # HANDLE FORM SUBMISSION
    # ======================================================

    if request.method == "POST":

        # --------------------------------------------------
        # GET FORM DATA
        # --------------------------------------------------

        name = request.POST.get(
            "name",
            "",
        ).strip()

        email = request.POST.get(
            "email",
            "",
        ).strip()

        phone = request.POST.get(
            "phone",
            "",
        ).strip()

        company = request.POST.get(
            "company",
            "",
        ).strip()

        service = request.POST.get(
            "service",
            "",
        ).strip()

        budget = request.POST.get(
            "budget",
            "",
        ).strip()

        message = request.POST.get(
            "message",
            "",
        ).strip()


        # ==================================================
        # VALIDATION
        # ==================================================

        if not name:

            messages.error(
                request,
                "Please enter your name.",
            )

            return render(
                request,
                "inquiries/contact.html",
            )


        if not email:

            messages.error(
                request,
                "Please enter your email address.",
            )

            return render(
                request,
                "inquiries/contact.html",
            )


        if not service:

            messages.error(
                request,
                "Please select a service.",
            )

            return render(
                request,
                "inquiries/contact.html",
            )


        if not message:

            messages.error(
                request,
                "Please tell us about your project.",
            )

            return render(
                request,
                "inquiries/contact.html",
            )


        # ==================================================
        # SAVE INQUIRY
        # ==================================================

        inquiry = Inquiry.objects.create(

            name=name,

            email=email,

            phone=phone,

            company=company,

            service=service,

            budget=budget,

            message=message,

        )


        # ==================================================
        # GET DISPLAY VALUES
        # ==================================================

        service_name = inquiry.get_service_display()


        if inquiry.budget:

            budget_name = inquiry.get_budget_display()

        else:

            budget_name = "Not specified"


        # ==================================================
        # EMAIL SUBJECT
        # ==================================================

        subject = (
            "New Customer Inquiry - "
            "NetCore TECH Solutions"
        )


        # ==================================================
        # EMAIL BODY
        # ==================================================

        email_message = f"""
NEW CUSTOMER INQUIRY
====================

A new project inquiry has been submitted
through the NetCore TECH Solutions website.


CUSTOMER INFORMATION
--------------------

Name:
{name}

Email:
{email}

Phone:
{phone if phone else "Not provided"}

Company / Organization:
{company if company else "Not provided"}


PROJECT INFORMATION
-------------------

Service Required:
{service_name}

Estimated Budget:
{budget_name}


CUSTOMER MESSAGE
----------------

{message}


INQUIRY STATUS
--------------

New


DATE RECEIVED
-------------

{inquiry.created_at.strftime("%B %d, %Y at %I:%M %p")}


ADMIN ACTION
------------

Please log in to the NetCore TECH Solutions
Django Admin Panel to review and manage this
customer inquiry.


NetCore TECH Solutions
Connecting technology, empowering businesses.
"""


        # ==================================================
        # SEND ADMIN EMAIL
        # ==================================================

        try:

            send_mail(

                subject=subject,

                message=email_message,

                from_email=settings.EMAIL_HOST_USER,

                recipient_list=[
                    settings.NETCORE_ADMIN_EMAIL,
                ],

                fail_silently=False,

            )

        except Exception as email_error:

            # ------------------------------------------------
            # IMPORTANT
            # ------------------------------------------------
            #
            # The inquiry has already been saved successfully.
            #
            # Therefore, an email failure must NOT delete
            # the customer's inquiry.
            #
            # The error is printed during development so we
            # can diagnose SMTP configuration problems.
            # ------------------------------------------------

            print(
                "NETCORE EMAIL ERROR:",
                email_error,
            )


        # ==================================================
        # CUSTOMER SUCCESS MESSAGE
        # ==================================================

        messages.success(

            request,

            (
                "Thank you! Your project request has "
                "been received successfully. Our team "
                "will get back to you soon."
            ),

        )


        # ==================================================
        # REDIRECT
        # ==================================================

        return redirect(
            "inquiries:contact",
        )


    # ======================================================
    # DISPLAY CONTACT PAGE
    # ======================================================

    return render(
        request,
        "inquiries/contact.html",
    )