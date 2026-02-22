from django import template
from django.utils.html import format_html

register = template.Library()

@register.filter
def availability_badge(is_available):
    if is_available:
        return format_html('<span class="badge bg-success me-2">In Stock</span>')
    return format_html('<span class="badge bg-danger me-2">Out of Stock</span>')