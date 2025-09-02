from django.contrib import admin
from .models import Perro

# Register your models here.
@admin.register(Perro)
class PerroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'raza', 'edad')
    search_fields = ('nombre', 'raza')
    list_filter = ('raza', 'edad')
    ordering = ('raza', 'edad')