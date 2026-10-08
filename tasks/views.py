from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def tasks(request):
    return render(request, 'tasks.html')

def contact(request):
    return render(request, 'contact.html')
