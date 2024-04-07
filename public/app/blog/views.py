from datetime import datetime
# Django
from django.views.generic import DetailView
from django.views.generic.list import ListView
# Application
from blog.models import Page, Category, Post


class BlogListView(ListView):
    model = Post
    queryset = Post.objects.filter(published_at__lte=datetime.now())
    template_name = "blog/index.html"


class CategoryListView(ListView):
    model = Post
    queryset = Post.objects.filter(published_at__lte=datetime.now())
    template_name = "blog/category.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(category_id=1)


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(published_at__lte=datetime.now())
    template_name = "blog/post.html"


class PageDetailView(DetailView):
    model = Page
    queryset = Page.objects.filter(published_at__lte=datetime.now())
    template_name = "blog/page.html"
