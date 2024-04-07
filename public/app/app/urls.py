"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Application
import app.views
import comment.views
import blog.views
import examination.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", app.views.welcome_view, name="home"),

    # Auth
    path('auth/', include("django.contrib.auth.urls")),
    path('auth/singup', user.views.signup, name="register"),

    # Profile
    path('profile', user.views.profile, name="my_profile"),
    path('profile/settings', user.views.settings, name="my_settings"),

    # Comment
    path("comment/add", comment.views.add_comment, name="add_comment"),

    # Blog
    path("blog", blog.views.BlogListView.as_view()),
    path("blog/category/<slug>", blog.views.CategoryListView.as_view(), name="category_view"),
    path("blog/post/<slug>", blog.views.PostDetailView.as_view(), name="post_view"),
    path("page/<slug>", blog.views.PageDetailView.as_view(), name="page_view"),

    # Examination
    path('examination/', examination.views.TestListView.as_view(), name="examination_list"),
    path('examination/my', examination.views.MyTestListView.as_view(), name="my_examination"),
    path('examination/new', examination.views.TestCreateView.as_view(success_url="/examination/my"),
         name="examination_new"),
    path('examination/<pk>/edit', examination.views.TestUpdateView.as_view(success_url="/examination/my"),
         name="examination_update"),
    path('examination/<pk>', examination.views.TestDetailView.as_view(), name="examination_view"),

    # API
    # * Auth
    path("api/auth/", include("djoser.urls.jwt")),
    # * User
    path("api/user/", include("user.api.urls")),
    # * blog
    path("api/blog/", include("blog.api.urls")),
    # * Comment
    path("api/comment", include("comment.api.urls")),
    # * Examination
    path("api/examination/", include("examination.api.urls")),
]
