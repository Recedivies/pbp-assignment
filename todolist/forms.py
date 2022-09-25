from django import forms


class TaskForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    description = forms.CharField(label="Description", widget=forms.Textarea)
