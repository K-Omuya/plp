from django import template

register = template.Library()

# Custom filter to split a string (file path) and return the last part (filename)
@register.filter(name='split_filename')
def split_filename(value):
    if isinstance(value, str):
        return value.split("/")[-1]  # Splits the string and returns the last part (filename)
    return value
