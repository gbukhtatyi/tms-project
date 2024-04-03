# Django
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.list import ListView
# Application
from .models import Test


class TestListView(ListView):
    queryset = Test.objects.filter(is_published=True)
    paginate_by = 1
    template_name = "examination/index.html"


class TestDetailView(DetailView):
    model = Test
    queryset = Test.objects.filter(is_published=True)
    template_name = "examination/view.html"


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


@login_required
def examination_export(request):
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


@login_required
def download_template():
    '''

    :return:
    '''

    pass
