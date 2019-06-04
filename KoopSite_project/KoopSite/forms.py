from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your full name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    comentarios = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'describe your request'}))


class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your user name'}))
    password = forms.CharField(widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your full name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'}))
    user = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your user name'}))
    password = forms.CharField(widget=forms.PasswordInput())
    password_conf = forms.CharField(label='Confirm password', widget=forms.PasswordInput())

    def clean_user_name(self):
        new_user = self.cleaned_data.get('user')
        qs = User.objects.filter(user=new_user)
        qs2 = User.objects.all()
        print(qs2)
        if qs.exists():
            raise forms.ValidationError('The username exists, please select a different one')
        return new_user

    def clean_email(self):
        new_email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=new_email)
        if qs.exists():
            raise forms.ValidationError('The email exists, please use a different one')
        return new_email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password_c = self.cleaned_data.get('password_conf')
        if password_c != password:
            raise forms.ValidationError('Passwords must match')
        return data
