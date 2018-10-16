from django.shortcuts import render

def home(request):
    return render(request, 'log/home.html')

def contact(request):
    return render(request, 'log/contact.html', {'title': 'Contact'})
