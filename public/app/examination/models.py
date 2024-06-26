# Django
from django.db import models
from django.contrib.auth import get_user_model
# Application
from .tasks import result_created


class Test(models.Model):
    # Relations
    user = models.ForeignKey(get_user_model(), null=True, default=None, on_delete=models.SET_DEFAULT,
                             verbose_name="Owner")
    # Data
    name = models.CharField(max_length=250, verbose_name="Навание")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    # Flags
    is_published = models.BooleanField(default=0, verbose_name="Опубликовано")

    def is_published_label(self):
        return 'Да' if self.is_published == True else 'Нет'


class QuestionType(models.TextChoices):
    ONE = 'one', 'Один правильный ответ'
    MULTIPLE = 'multiple', 'Множественный правильный ответ'


class Question(models.Model):
    # Relations
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    # Data
    type = models.CharField(max_length=16, choices=QuestionType, default=QuestionType.ONE, verbose_name="Тип вопроса")
    content = models.CharField(max_length=1024, verbose_name="Вопрос")


class Answer(models.Model):
    # Relations
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Question")
    # Data
    content = models.CharField(max_length=1024, verbose_name="Ответ")
    score = models.IntegerField(default=0, verbose_name="Балл")


class ResultStatus(models.TextChoices):
    NEW = 'new', 'Новое тестирование'
    FINISHED = 'finished', 'Тестирование завершено'


class Result(models.Model):
    # Relations
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, verbose_name="Owner", default=0)
    test = models.ForeignKey(Test, on_delete=models.PROTECT, verbose_name="Test")
    # Data
    status = models.CharField(max_length=16, choices=ResultStatus, default=ResultStatus.NEW,
                              verbose_name="Статус тестирования")
    score = models.IntegerField(default=0)
    score_total = models.IntegerField(default=0)
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        is_creating = self.id is None
        super().save(**kwargs)
        if self.status == ResultStatus.FINISHED:
            result_created.apply_async(args=[self.id])

    class Meta:
        ordering = ['-created_at']


class ResultAnswer(models.Model):
    # Relations
    result = models.ForeignKey(Result, on_delete=models.CASCADE, verbose_name="Result")
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name="Question")
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT, verbose_name="Answer")
