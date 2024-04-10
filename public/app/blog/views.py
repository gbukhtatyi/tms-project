from datetime import datetime
# Django
from django.shortcuts import get_object_or_404
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
        return qs.filter(category__slug=self.kwargs.get('slug'))

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['category'] = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return context


class PostDetailView(DetailView):
    model = Post
    queryset = Post.objects.filter(published_at__lte=datetime.now())
    template_name = "blog/post.html"


class PageDetailView(DetailView):
    model = Page
    queryset = Page.objects.filter(published_at__lte=datetime.now())
    template_name = "blog/page.html"
