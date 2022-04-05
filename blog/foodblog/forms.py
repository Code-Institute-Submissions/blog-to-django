from django import forms
from .models import Blog


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'dish', 'author', 'card')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'dish': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name of dish'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'card': forms.Textarea(attrs={'class': 'form-control'}),
        }