from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.

def register(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            if User.objects.filter(email = email).exists():
                messages.info(request, "email already exist try with another email")
                print("false1")
                return redirect('register')
            elif User.objects.filter(username = username):
                messages.info(request, "username already taken")
                print("false1")
                return redirect('register')
            else:
                 user = User.objects.create_user(username= username, first_name = first_name, last_name = last_name, email = email, password= password)
                 user.save();
                 print('user created')
                 return redirect('/')        

       
    else:
        return render(request,'travelmate/register.html',)

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            return redirect('/')
        else:
            messages.error(request,'Invalid Credential')
            return redirect('login')


    else:
        return render(request, 'travelmate/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')  