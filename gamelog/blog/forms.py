from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'content']
        labels = {
            'title': 'Título',
            'content': 'Contenido',
        }
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 15,
                'class': 'markdown-editor',
                'placeholder': 'Write your post in Markdown...\n\n# Heading 1\n## Heading 2\n\n**bold** *italic*\n\n- List item\n- Another item\n\n```python\nprint("Code block")\n```'
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user