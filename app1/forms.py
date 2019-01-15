from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class RegistrForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    password_ver = forms.CharField(widget=forms.PasswordInput())


class SearchForm(forms.Form):
    dep = forms.CharField(required=False, max_length=50)
    acc = forms.CharField(required=False, max_length=50)
    ddt = forms.DateField(required=False)


class ProfForm(forms.Form):
    firstname = forms.CharField(required=False, max_length=30)
    lastname = forms.CharField(required=False, max_length=150)
    email = forms.EmailField(required=False)
    about = forms.CharField(required=False)


class ImageUploadForm(forms.Form):
    image = forms.ImageField()
