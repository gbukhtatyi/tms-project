from django.apps import apps
from django.conf import settings
from django.http import Http404


def get_app_label(type: str):
    if (type in settings.DYNAMIC_OBJECT_TYPES):
        return settings.DYNAMIC_OBJECT_TYPES[type]
    raise Http404


def get_dynamic_model_class(type: str):
    '''
    Получение класса модели
    :param type:
    :param id:
    :return:
    '''

    return apps.get_model(
        get_app_label(type),
        type
    )


def get_dynamic_model(type: str, id: int):
    model_class = get_dynamic_model_class(type)
    queryset = model_class.objects.filter(id=id)
    try:
        model = queryset.get()
    except queryset.model.DoesNotExist:
        raise Http404("No models found matching the query")

    return model
