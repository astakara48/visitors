from django.contrib import admin
from .models import Visitor

# Register your models here.

class VisitorAdmin(admin.ModelAdmin):
    list_display = ['name', 'number', 'number2', 'date', 'pk', 'check', 'image', ]

admin.site.register(Visitor, VisitorAdmin)