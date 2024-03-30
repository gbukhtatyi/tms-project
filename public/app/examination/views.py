# Django
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Application
from models import Test


@login_required
def examination_import(request):
    '''

    :param request:
    :return:
    '''
    errors = []

    if request.method != "POST":
        pass

    return render(
        request,
        "examination/import.html",
        {
            errors: errors
        }
    )
