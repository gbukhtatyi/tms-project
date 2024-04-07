from django.db import models
from django.contrib.auth import get_user_model


class Test(models.Model):
    # Relations
    user = models.ForeignKey(get_user_model(), null=True, default=None, on_delete=models.SET_DEFAULT, verbose_name="Owner")
    # Data
    name = models.CharField(max_length=250, verbose_name="Навание")
    description = models.CharField(max_length=1024, verbose_name="Описание")
    # Flags
    is_published = models.BooleanField(default=0, verbose_name="Опубликовано")

    def is_published_label(self):
        return 'Да' if self.is_published == True else 'Нет'


class Question(models.Model):
    # Relations
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Тест")
    # Data
    type = models.CharField(max_length=16, verbose_name="Тип вопроса")
    content = models.CharField(max_length=1024, verbose_name="Вопрос")


class Answer(models.Model):
    # Relations
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Question")
    # Data
    content = models.CharField(max_length=1024, verbose_name="Ответ")
    score = models.IntegerField(default=0, verbose_name="Балл")


class Result(models.Model):
    # Relations
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, verbose_name="Owner", default=0)
    test = models.ForeignKey(Test, on_delete=models.PROTECT, verbose_name="Test")
    score = models.IntegerField(default=0)
    score_total = models.IntegerField(default=0)


class ResultAnswer(models.Model):
    # Relations
    result = models.ForeignKey(Result, on_delete=models.CASCADE, verbose_name="Result")
    question = models.ForeignKey(Question, on_delete=models.PROTECT, verbose_name="Question")
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT, verbose_name="Answer")
