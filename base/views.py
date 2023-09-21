from django.shortcuts import redirect, render
from .models import Project
from .forms import ContactForm

def home(request):
    context = {}
    return render(request, 'base/home.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'base/portfolio.html', context)

def project(request, pk):
    project = Project.objects.get(id=pk)
    context = {
        'project': project
    }
    return render(request, 'base/project.html', context)

def contact(request):
    form = ContactForm()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'base/contact.html', {'form': form})
