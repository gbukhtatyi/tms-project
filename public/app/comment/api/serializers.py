# Django Rest
from rest_framework import serializers
# Application
from comment.models import Comment
from user.api.serializers import UserSerializer


class CommentListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ["content", "user"]

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ["type_source", "type_id", "content", "user"]
