from django.contrib import admin

from .models import Task, Test

# Register your models here.

admin.site.register(Test)
admin.site.register(Task)
