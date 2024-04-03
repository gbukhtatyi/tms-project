from django.db import models
from django.contrib.auth import get_user_model


class Test(models.Model):
    # Relations
    user = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, verbose_name="Owner", default=0)
    # Data
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=1024)
    # Flags
    is_published = models.BooleanField(default=0)


class Question(models.Model):
    # Relations
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Test")
    # Data
    type = models.CharField(max_length=16)
    content = models.CharField(max_length=1024)


class Answer(models.Model):
    # Relations
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Question")
    # Data
    content = models.CharField(max_length=1024)
    score = models.IntegerField(default=0)


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
