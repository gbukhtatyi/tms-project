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
import blog.views
import examination.views
import user.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", app.views.welcome_view, name="home"),

    # Auth
    path('auth/', include("django.contrib.auth.urls")),
    path('auth/singup', user.views.signup, name="register"),

    # Blog
    path("blog", blog.views.blog_category_index),
    path("blog/category/<slug>", blog.views.blog_category_view),
    path("blog/post/<slug>", blog.views.blog_post_view),

    # Examination
    path('examination/', examination.views.TestListView.as_view(), name="examination_list"),
    path('examination/<pk>', examination.views.TestDetailView.as_view(), name="examination_view"),
]
