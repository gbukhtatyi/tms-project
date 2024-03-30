from datetime import datetime
# Django
from django.http import Http404
from django.shortcuts import render, get_object_or_404
# Application
from blog.models import Page, Category, Post


def blog_page_view(request, slug):
    '''

    :param request:
    :param slug:
    :return:
    '''
    page = get_object_or_404(Page, slug=slug)

    return render(
        request,
        "blog/page.html",
        {
            "post": page
        }
    )


def blog_category_view(request, slug):
    '''

    :param request:
    :param slug:
    :return:
    '''
    category = get_object_or_404(Category, slug=slug)

    return render(
        request,
        "blog/category.html",
        {
            "category": category
        }
    )


def blog_post_view(request, slug):
    '''

    :param request:
    :param slug:
    :return:
    '''
    post = get_object_or_404(Post, slug=slug)

    if (post.updated_at <= datetime.now()):
        raise Http404("Post does not exist")

    return render(
        request,
        "blog/post.html",
        {
            "post": post
        }
    )
