from django.shortcuts import render, redirect
from .models import Job 
from .employer_form import JobForm

# Create your views here.
def display_home(request):
    return render(request, 'home.html', {})

def display_about(request):
    return render(request, 'about.html', {})

def display_category(request):
    job = Job.objects.all()
    return render(request, 'category.html', {'Jobs': job})

def job_desc(request, job_id):
    job = Job.objects.get(pk=job_id)
    job.salary = "{:,}".format(job.salary)
    return render(request, 'job_detail.html', {'job': job})   

def job_new(request):
    if request.method == "POST":
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save
            form.save()
            return redirect('category')
    else:
        form = JobForm()
    return render(request, 'employer_form.html', {'form': form})

