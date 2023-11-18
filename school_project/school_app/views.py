from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth


# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new')
        else:
            messages.info(request, 'Invalid credentials!')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                print('User created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching!')
            return redirect('register')
    return render(request, 'Register.html')

def new(request):
    return render(request, 'new.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
