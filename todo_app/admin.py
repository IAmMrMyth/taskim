from django.contrib import admin
from .models import TodoItem
# Register your models here.


class TodoitemAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_done']
    list_filter = ['is_done', 'created_date']


admin.site.register(TodoItem, TodoitemAdmin)
