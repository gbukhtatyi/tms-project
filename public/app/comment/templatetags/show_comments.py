from django import template
# Application
from comment.forms import CommentForm
from comment.models import Comment

register = template.Library()


@register.inclusion_tag('comment/form.html', takes_context=True)
def new_comments(context, model):
    return {
        "next_path": context.request.path,
        "form": CommentForm({
            "type_source": model._meta.model_name,
            "type_id": model.id,
            "content": "Введите текст комментария"
        })
    }


@register.inclusion_tag('comment/show.html', takes_context=True)
def show_comments(context, model):
    comments = Comment.objects.filter(
        type_source=model._meta.model_name,
        type_id=model.id
    )

    return {
        "type_source": model._meta.model_name,
        "type_id": model.id,
        "comments": comments
    }
