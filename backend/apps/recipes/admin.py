from django.contrib import admin

# Register your models here.
from .models import Recipe, Tag

admin.site.register(Recipe)
admin.site.register(Tag)
