from django import forms
from .models import Post, Comment, ReComment

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'img']


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['content']


class ReCommentForm(forms.ModelForm):

    class Meta:
        model = ReComment
        fields = ['content']
