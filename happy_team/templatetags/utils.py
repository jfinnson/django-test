from django import template

register = template.Library()


@register.filter
def get_key_value(some_dict, key):
    """
    Provides a filter to be used in Django Jinja2 templates.
    Filter allows lookup of values within a dictionary {} via a key.
    :param some_dict: Dictionary object
    :param key: key value to lookup in some_dict
    :return: value in dict at key
    """
    return some_dict.get(key, '')
