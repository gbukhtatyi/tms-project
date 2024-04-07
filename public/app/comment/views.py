# Django
from django import template
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from comment.forms import CommentForm
# Application
from comment.models import Comment

register = template.Library()


@login_required
def add_comment(request):
    form = CommentForm(request.POST,initial={"user": request.user})
    if form.is_valid():
        form.save()
    return HttpResponseRedirect(request.POST.get('next', '/'))


@register.inclusion_tag('comment/show.html', takes_context=True)
def show_comments(context, model):
    type_source = model._meta.model_name

    comments = Comment.objects.filter(
        type_source=type_source,
        type_id=model.id
    )

    return {
        "type_source": type_source,
        "type_id": model.id,
        "comments": comments
    }
