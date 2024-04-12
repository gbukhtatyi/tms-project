# Celery
from celery import shared_task
# Django
from django.apps import apps as django_apps
from django.core.mail import send_mail
from django.utils.html import strip_tags


@shared_task
def result_created(result_id: int):
    Result = django_apps.get_model(app_label='examination', model_name='Result')
    result_model = Result.objects.get(id=result_id)
    test = result_model.test
    user = result_model.user

    if result_model is None:
        return;

    html_message = f"<p>Date: {result_model.created_at}</p> Ваш балл: {result_model.score} из {result_model.score_total}"
    plain_message = strip_tags(html_message)

    send_mail(
        f"[Test App] Ваш результат тестирования: {test.name}",
        plain_message,
        "info@project.local",
        [user.email],
        fail_silently=False,
        html_message=html_message
    )
