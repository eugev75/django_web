from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','Descriptions','important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'write a title'}),
            'Descriptions': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'write a Descriptions'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check m-auto'}),
        }
 
