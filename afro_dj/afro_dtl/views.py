from django.shortcuts import render

def index(request):
    p_title = 'Afro Django'
    return render(request, 'index.html', {'p_title': p_title})
