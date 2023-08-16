from django import template
import os
register = template.Library()
#@register.filter(name="ext")
@register.filter()

def ext(value):
    root, ext = os.path.splitext(value)
    ext = ext.replace('.','')
    return ext
