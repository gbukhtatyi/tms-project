# Django
from django.views.decorators.csrf import csrf_exempt
# Django Rest
from rest_framework import generics
# Application
from comment.api.serializers import CommentSerializer, CommentListSerializer
from comment.models import Comment


class CommentListCreateView(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CommentSerializer
        return CommentListSerializer

    def get_queryset(self):
        model_type = self.request.data.get('type_source')
        model_type_id = self.request.data.get('type_id')

        return Comment.objects.filter(
            type_source=model_type,
            type_id=model_type_id
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
