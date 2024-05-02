from django import template

register = template.Library()

@register.simple_tag
def breadcrumb_schema():
    return "http://schema.org/BreadcrumbList"

@register.inclusion_tag('')