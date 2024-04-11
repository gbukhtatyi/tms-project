# Django
from django.contrib import admin

from examination.models import Test, Question, Answer


# Application


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = [
        # Relations
        "user",
        # Data
        "name",
        "description",
        # Flags
        "is_published",
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        # Relations
        "test",
        # Data
        "type",
        "content",
    ]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = [
        # Relations
        "question",
        # Data
        "content",
        "score",
    ]
