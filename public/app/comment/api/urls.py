from django.urls import path
from . import views

urlpatterns = [
    path('', views.CommentListCreateView.as_view(), name="api_comment_view"),
]
