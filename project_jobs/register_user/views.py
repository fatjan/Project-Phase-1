from django.shortcuts import render, redirect
from .forms import DocumentForm

def form_register(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'user_register.html', {
        'form': form
    })