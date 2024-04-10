# Django
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.db.models import Q
# Application
from .models import Test, Question, Answer


class TestListView(ListView):
    queryset = Test.objects.filter(is_published=True)
    paginate_by = 20
    template_name = "examination/index.html"


class TestDetailView(DetailView):
    model = Test
    template_name = "examination/view.html"

    def get_queryset(self, **kwargs):
        qs = super().get_queryset(**kwargs)
        if (self.request.user):
            qs = qs.filter(Q(is_published=True) | Q(user=self.request.user))
        else:
            qs = qs.filter(is_published=True)
        return qs


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
    template_name = "examination/test/form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TestUpdateView(UpdateView):
    model = Test
    fields = ["name", "description", "is_published"]
    template_name = "examination/test/form.html"

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(user_id=self.request.user.id)


class QuestionCreateView(CreateView):
    model = Question
    fields = ["type", "content"]
    template_name = "examination/question/form.html"

    def get(self, request, *args, **kwargs):
        self.test_id = self.kwargs.get('pk')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.test_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('question_update', kwargs={'pk': self.object.question_id})


class QuestionUpdateView(UpdateView):
    model = Question
    fields = ["type", "content"]
    template_name = "examination/question/form.html"

    def get(self, request, *args, **kwargs):
        self.test_id = kwargs.get('pk')
        return super().get(request, *args, **kwargs)

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(test__user_id=self.request.user.id)

    def get_success_url(self):
        return reverse('question_update', kwargs={'pk': self.object.id})


class QuestionRemoveView(DeleteView):
    model = Question

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(test__user_id=self.request.user.id)

    def get_success_url(self):
        return reverse('examination_update', kwargs={'pk': self.object.test.id})


def save_question_answers(request, pk):
    correct_answers_id = request.POST.getlist('answers[]')

    Answer.objects.filter(question_id=pk).update(score=0)
    Answer.objects.filter(question_id=pk).filter(id__in=correct_answers_id).update(score=1)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


class AnswerCreateView(CreateView):
    model = Answer
    fields = ["content"]
    template_name = "examination/answer/form.html"

    def get(self, request, *args, **kwargs):
        self.question_id = self.kwargs.get('pk')
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.question_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('question_update', kwargs={'pk': self.object.question.id})


class AnswerUpdateView(UpdateView):
    model = Answer
    fields = ["content"]
    template_name = "examination/answer/form.html"

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(question__test__user_id=self.request.user.id)

    def get_success_url(self):
        return reverse('question_update', kwargs={'pk': self.object.question.id})


class AnswerRemoveView(DeleteView):
    model = Answer

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

    def get_queryset(self, **kwargs):
        return super().get_queryset(**kwargs).filter(question__test__user_id=self.request.user.id)

    def get_success_url(self):
        return reverse('question_update', kwargs={'pk': self.object.question.id})


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
