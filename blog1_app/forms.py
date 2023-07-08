# yeha chai django le default provide garne forms

from django import forms

from blog1_app.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content',)
    