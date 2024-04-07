from django.shortcuts import render


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
