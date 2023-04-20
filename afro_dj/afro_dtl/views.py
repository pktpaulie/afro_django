from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import CustomMessage, UserAccount
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


'''
Using Django Templating Language, design a custom form that 
captures user data or input, posts the data to a view which then 
redirects the user to a new 
template displaying the data as django templating variables.
'''
def user_msg(request):
    #contact_form = MessageForm(data=request.POST)
    if request.method == 'POST':
        #if form.is_valid():
        #contact_form = MessageForm(data=request.POST)
        my_email = request.POST.get('my_email')
        #my_email = request.POST['m_email']
        title = request.POST.get('title')
        #title = request.POST['title']
        my_msg = request.POST.get('my_msg')
        msg_details = CustomMessage(my_email=my_email, title=title, my_msg=my_msg)
        msg_details.save()
        print(my_email + ' ' + 'message sent')
        messages.success(request, 'Message sent successfully')
        #return redirect('msg_disp')
        return render(request, 'msg_disp.html')
    else:
        return render(request, 'contact_us.html')

def msg_disp(request):
    #msg = get_object_or_404(Message, pk=pk)
    
    msgs = CustomMessage.objects.all
    print('Messages')
    context = {
        'title': "Your Messages",
        'msgs': msgs,
        # 'msg_save': msg_save,
        # 'my_title': my_title,
    }
    return render(request, 'msg_disp.html', {'msgs': msgs})
