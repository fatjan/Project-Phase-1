from django.shortcuts import render

# Create your views here.
def display_home(request):
    return render(request, 'home.html', {})

def display_about(request):
    return render(request, 'about.html', {})

def display_category(request):
    return render(request, 'category.html', {})