from django.shortcuts import render
from .models import Home

def home(request):
    home = Home.objects.all()
    return render(request, 'home.html', {'home':home})
