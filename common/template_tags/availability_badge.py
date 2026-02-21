from django import template

register = template.Library()

@register.simple_tag
def availability_badge(is_available):
    if is_available:
        return '<span class="badge bg-success">In Stock</span>'
    else:
        return '<span class="badge bg-danger">Out of Stock</span>'