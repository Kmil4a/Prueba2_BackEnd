from django import forms
from .models import ToDo


class FormTodo(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ['title']

        labels = {
            'title': 'Titulo de la tarea',

        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Hacer la tarea...'}),
        }
