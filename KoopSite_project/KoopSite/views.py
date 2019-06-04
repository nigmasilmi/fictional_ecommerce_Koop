from django.shortcuts import render, redirect
from .forms import ContactForm, LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model


def home(request):
    template_name = 'index.html'
    title = 'Koop Products Best Quality from China'
    return render(request, template_name, {'title': title})


def about_view(request):
    template_name = 'about.html'
    title = 'About our company'
    return render(request, template_name, {'title': title})


def login_view(request):
    ''' verifies if the user is logged in, if not, asks for registration'''
    title = 'Log in as user'
    login_form = LoginForm(request.POST or None)
    context = {
        'title': title,
        'form': login_form
    }
    template_name = 'login.html'
    print('the user is authenticated 1: ' + str(request.user.is_authenticated))
    if login_form.is_valid():
        print(login_form.cleaned_data)
        username = login_form.cleaned_data.get('user')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        print(username)
        print(password)
        print('the user is authenticated 2: ' + str(request.user.is_authenticated))
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        else:
            # Return an 'invalid login' error message.
            print('Error')
            return redirect('/')

    return render(request, template_name, context)


User = get_user_model()


def register_view(request):
    register_form = RegisterForm(request.POST or None)
    template_name = 'register.html'
    title = 'Register as user'
    context = {
        'title': title,
        'form': register_form
    }
    if register_form.is_valid():
        new_name = register_form.cleaned_data.get('name')
        new_username = register_form.cleaned_data.get('user')
        new_email = register_form.cleaned_data.get('email')
        # print(register_form.cleaned_data)
        new_user = User.objects.create_user(new_name, new_username, new_email)
        print(new_user)
        # new_user.save()

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
        contact_form = ContactForm()
        return redirect('/')
    return render(request, template_name, context)
