from django import template

register = template.Library()


@register.filter(name='change_name')
def change_name(value, index):
    if value and index <= len(value):
        return value.replace(value[index], 'yupeng')
    else:
        return value
