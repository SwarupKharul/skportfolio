from django.shortcuts import render
from .models import Project


def home(request):
    return render(request, 'index.html')

def project(request):
    projects = Project.objects.all()
    return render(request, 'projects-grid-cards.html', {'projects':projects})

def cv(request):
    return render(request, 'cv.html')

