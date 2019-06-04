from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'your full name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'describe your request'}))
    comentarios = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'describe your request'}))


class LoginForm(forms.Form):
    user = forms.CharField()
    password = forms.PasswordInput()
