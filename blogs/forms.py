from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {'title': '', 'content': ''}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}
