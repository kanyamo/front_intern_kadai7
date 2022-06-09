from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ("title", "contents", "deadline_date", "deadline_time")
        widgets = {
            "deadline_date": forms.SelectDateWidget
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['deadline_time'].widget.attrs['placeholder'] = '例)06:55'
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['contents'].widget.attrs['class'] = 'form-control textarea'
        self.fields['deadline_date'].widget.attrs['class'] = 'date-form'
        self.fields['deadline_time'].widget.attrs['class'] = 'time-form'
