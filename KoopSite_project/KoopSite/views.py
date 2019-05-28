from django.shortcuts import render


def home(request):
    template_name = 'index.html'
    title = 'Koop Products Best Quality from China'
    return render(request, template_name, {'title':title})
