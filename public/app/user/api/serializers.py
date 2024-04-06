# Django
from django.contrib.auth import get_user_model
# Django Rest
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'first_name', 'last_name', 'email']


class UserSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['is_subscribed']
