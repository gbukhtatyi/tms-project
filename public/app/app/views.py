from django.shortcuts import render, get_object_or_404


def welcome_view(request):
    '''
    Главная страница сайта
    :param request:
    :return:
    '''
    return render(
        request,
        "welcome.html",
    )
