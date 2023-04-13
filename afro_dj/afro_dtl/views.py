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
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    gender = request.POST['gender']
    user_details = [username, email, password, gender]
    print(user_details)
    return render(request, 'index.html', {'username': username})
    
    