from django.contrib import admin
from .models import Shoe, Category, Tag

# Register your models here.
admin.site.register(Shoe)
admin.site.register(Category)
admin.site.register(Tag)