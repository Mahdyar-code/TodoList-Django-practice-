from django import forms
from task.models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description','priority','due_date')

        widgets = {
            'title': forms.TextInput(attrs={'placeholder':'e.g. Learn Django Forms',}),
            'description': forms.Textarea(attrs={'placeholder':'input a short description ','rows':6}),
            'due_date': forms.DateInput(attrs={'type':'date'}),
        }