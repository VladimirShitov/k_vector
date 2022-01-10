from django import template

register = template.Library()


@register.simple_tag
def get_samples_list():
    from pathology.utils import get_categories_content
    return get_categories_content()
