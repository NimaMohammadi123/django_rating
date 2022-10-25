from django import forms
from .models import Post


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comment = forms.CharField(widget=forms.Textarea,required=False)

class Post_Form(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['rating',]

class Rating_Form(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['rating',]
