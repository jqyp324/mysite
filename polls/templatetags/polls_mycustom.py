from django import template
import datetime

register = template.Library()


@register.filter(name='change_name')
def change_name(value, index):
    if value and index <= len(value):
        return value.replace(value[index], 'yupeng')
    else:
        return value


@register.simple_tag(name='nowtime')
def current_time():
    return str(datetime.datetime.now())

# print(type(str(datetime.datetime.now())))
