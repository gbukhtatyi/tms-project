from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_comment, name="api_comment_view"),
]
