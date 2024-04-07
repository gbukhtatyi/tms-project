from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name="api_user_profile"),
    path('settings', views.settings, name="api_user_settings"),
]
