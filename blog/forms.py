from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            'name': 'Nome',
            'email': 'E-mail',
            'body': 'Comentário'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input p-2 border rounded shadow mb-4'}),
            'email': forms.EmailInput(attrs={'class': 'input p-2 border rounded shadow mb-4'}),
            'body': forms.Textarea(attrs={'class': 'textarea resize-none p-2 shadow mb-4'}),
        }