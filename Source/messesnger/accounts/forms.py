from django.contrib.auth.models import User
from django import forms
from .models import Post


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Give me a Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Give me a Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Give me a e-mail'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Give me a Password'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Give me a Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Give me a e-mail'}))


class PostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Please share a Post!!!'})
    )

    class Meta:
        model = Post
        fields = {'post',}

