# Django
from django.views.decorators.csrf import csrf_exempt
# Rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Application
from comment.services import add_comment


@csrf_exempt
@api_view(["POST"])
def create_comment(request):
    '''
    Добавление комментария к выбранной модели
    :param model:
    :return:
    '''

    model_type = request.data.get('type')
    model_type_id = request.data.get('type_id')
    content = request.data.get('content')

    add_comment(
        request.user.id,
        model_type,
        model_type_id,
        content
    )

    return Response(
        data={"status": "ok"},
        status=201
    )
