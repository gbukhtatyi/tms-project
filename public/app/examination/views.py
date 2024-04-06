# Django
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
# Application
from .models import Test


class TestListView(ListView):
    queryset = Test.objects.filter(is_published=True)
    paginate_by = 20
    template_name = "examination/index.html"


class TestDetailView(DetailView):
    model = Test
    queryset = Test.objects.filter(is_published=True)
    template_name = "examination/view.html"


class MyTestListView(ListView):
    queryset = Test.objects.all()
    paginate_by = 20
    template_name = "examination/grid.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        return qs.filter(user_id=self.request.user.id)

class TestCreateView(CreateView):
    model = Test
    fields = ["name", "description", "is_published"]
    template_name = "examination/form.html"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TestUpdateView(UpdateView):
    model = Test
    fields = ["name", "description", "is_published"]
    template_name = "examination/form.html"

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
