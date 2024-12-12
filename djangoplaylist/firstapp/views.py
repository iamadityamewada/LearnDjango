from django.shortcuts import render
# from django.http import HttpResponse



# Create your views here.

def home(request):
    # return HttpResponse("Hello World")
    return render(request, 'djangoplaylist/home.html', {"name":"Aditya"})

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int(val1) + int(val2)
    return render(request, 'djangoplaylist/add.html', {'result':res})