from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import UserAccount
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    p_title = 'Afro Django'
    
    if request.user.is_authenticated:
        username = request.user.username
        context = {
            'p_title': p_title,
            'username': username,
        }
        return render(
            request, 
            'index.html', 
            context=context)
    else:    
        author = 'Pauline'
        gender = 'Female'
        context = {
            'p_title': p_title,
            'author': author,
            'gender': gender,
        }
        return render(request, 'index.html', context=context)

def register(request):
    return render(request, 'register.html')

def registration(request):
    user_name = request.POST['username']
    email = request.POST['user_email']
    password = request.POST['password']
    gender = request.POST['gender']
    user_details = [user_name, email, password, gender]
    print(user_details)
    if User.objects.filter(username=user_name).first():
        print(user_name + ' already exists')
        return render(request, 'login.html')
    else:
        user = User.objects.create_user(user_name, email, password)
        return render(request, 'login.html')

    #return render(request, 'index.html', {'username': username})
    
def login_user(request):
    user_name = request.POST['username']
    pwd = request.POST['password']
    if User.objects.filter(username=user_name):
        print(user_name + ' already exists')
        logged_user = authenticate(request, username=user_name, password=pwd)
        if logged_user is not None:
            #login the user
            auth_login(request, logged_user)
            print(user_name + ' ' + 'logged in successfully')
            messages.success(request, 'You have logged in successfully. Welcome!')
            return redirect('index')
        else:
            # where authentication has failed/ user credentials do not exist
            return render(request, 'login.html')
    else:
        print('User credentials do not exist')
        return render(request, 'login.html')



def login_page(request):
    return render(request, 'login.html')


'''
if request=='POST':
        user_name = request.POST['username']
        pwd = request.POST['password']
        if User.objects.filter(username=user_name).first():
            print(user_name + ' already exists')
            logged_user = authenticate(request, username=user_name, password=pwd)
            if logged_user is not None:
                #login the user
                auth_login(request, logged_user)
                print(user_name + ' ' + 'logged in successfully')
                return redirect('index/')
            else:
                # where authentication has failed/ user credentials do not exist
                return render(request, 'login.html')
        else:
            print('User credentials do not exist')
            return render(request, 'login.html')
    else:
        pass
'''

@login_required
def logout_user(request):
    auth_logout(request)
    messages.error(request, 'You have logged out successfully. Goodbye!')
    return redirect('login_page')