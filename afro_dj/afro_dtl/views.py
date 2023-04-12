from django.shortcuts import render

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
