from django.shortcuts import render
from .models import project
# Create your views here.
def home(request):
    projectss=project.objects.all()
    return render(request,'portfolio/home.html',{'projects':projectss})
def about(request):
    return render(request,'portfolio/about.html')