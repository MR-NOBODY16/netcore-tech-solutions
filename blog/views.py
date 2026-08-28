from django.shortcuts import get_object_or_404

from django.shortcuts import render

from .models import Post


def blog_home(request):

    posts = (
        Post.objects
        .filter(
            is_published=True,
        )
        .order_by(
            "-featured",
            "-published_at",
            "-created_at",
        )
    )


    featured_posts = posts.filter(
        featured=True,
    )


    return render(
        request,
        "blog/blog.html",
        {
            "posts": posts,
            "featured_posts": featured_posts,
        },
    )


def post_detail(
    request,
    slug,
):

    post = get_object_or_404(
        Post,
        slug=slug,
        is_published=True,
    )


    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
        },
    )