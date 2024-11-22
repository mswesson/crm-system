from django import template

register = template.Library()


@register.filter
def map(value, arg):
    """
    Применяет атрибут arg ко всем элементам value,
    если это QuerySet или список объектов.

    Например, user.groups.all|map:"name" вернет список
    всех имен групп пользователя.
    """
    return [getattr(item, arg, None) for item in value]
