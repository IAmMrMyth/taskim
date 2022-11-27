from django import forms
from .models import TodoItem

widget = {
    'title': forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter title of task'
    }),
    'description': forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Enter description of task'
    })
}


class TodoItemCreateForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ['title', 'description']
        widgets = widget


class TodoItemUpdateForm(forms.ModelForm):
    class Meta:
        model = TodoItem
        fields = ["title", "description", "is_done", "archive"]
        widgets = widget
