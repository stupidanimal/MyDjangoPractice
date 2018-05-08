from django import forms
from .models import BlogItems


class BlogItemForm(forms.ModelForm):
    class Meta:
        model = BlogItems
        fields = ['title', 'content']
        labels = {'title': '', 'content': ''}
        widgets = {
            'content': forms.Textarea(
                attrs={'cols': 100, 'rows': 10, 'max_length': 500, 'placeholder': 'input blog content', 'class': 'form-control'}),
            'title': forms.TextInput(attrs={'placeholder': 'input blog title', 'class': 'form-control'})}
