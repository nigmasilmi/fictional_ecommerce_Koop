from django.shortcuts import render
from .forms import ContactForm, LoginForm


def home(request):
    template_name = 'index.html'
    title = 'Koop Products Best Quality from China'
    return render(request, template_name, {'title': title})


def about_view(request):
    template_name = 'about.html'
    title = 'About our company'
    return render(request, template_name, {'title': title})


def login_view(request):
    login_form = LoginForm(request.POST or None)
    template_name = 'login.html'
    title = 'Log in as user'
    context = {
        'title': title,
        'form': login_form
    }
    if login_form.is_valid():
        print(login_form.cleaned_data)
    return render(request, template_name, context)


def register_view(request):
    login_form = LoginForm(request.POST or None)
    template_name = 'register.html'
    title = 'Register as user'
    context = {
        'title': title,
        'form': login_form
    }
    return render(request, template_name, context)


def contact_view(request):
    template_name = 'contact.html'
    contact_form = ContactForm(request.POST or None)
    title = 'Contact the supplier'
    context = {
        'title': title,
        'form': contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, template_name, context)
