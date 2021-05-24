from django import template
from search.choices import choices

register = template.Library()


@register.filter
def translate_data(value):
    """
    Returns value or it's verbose version.

    choices is a dict.

    Usage::

        {% load translate %}
        {{data|translate}}
    """
    return choices.get(value, value)
