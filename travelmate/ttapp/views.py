from django.shortcuts import render
from .models import destination
# Create your views here.

def home(request):
    dests = destination.objects.all()
    return render(request, 'travelmate/index.html', {'dests':dests})