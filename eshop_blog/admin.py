from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    row_id_fields=('category',)