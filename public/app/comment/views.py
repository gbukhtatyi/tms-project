from django import template

register = template.Library()


@register.inclusion_tag('comment/show.html')
def show_comments(model):
    return {
        model: model
    }
