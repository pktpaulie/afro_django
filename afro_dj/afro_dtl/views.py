from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout


def index(request):
    p_title = 'Afro Django'
    username = 'Pauline'
    gender = 'Female'
    return render(
        request, 
        'index.html', 
        {'p_title': p_title,
         'username': username,
         'gender': gender})

def register(request):
    return render(request, 'register.html')

def registration(request):
    if request == 'POST':
        name = request.POST.get['username']
        email = request.POST.get['email']
        password = request.POST.get['password']
        gender = request.POST.get['gender']
        user_details = ['name', 'email', 'password', 'gender']
        print(user_details)
    else:
        pass
