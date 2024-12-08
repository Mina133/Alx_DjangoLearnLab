from django import forms
from django.contrib.auth.models import User
from .models import Profile, Comment, Post
from taggit.forms import TagField, TagWidget
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class PostForm(forms.ModelForm):
    tags = TagWidget()

    class Meta:
        model = Post
        fields = ['title', 'content', 'tag']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
