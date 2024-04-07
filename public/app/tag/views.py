from django import template

register = template.Library()


@register.inclusion_tag('tag/show.html')
def show_tags(model):
    return {
        model: model
    }
