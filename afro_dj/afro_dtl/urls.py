from django.urls import path
from . import views
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('registration/', views.registration, name='registration'),
    path('login_user/', views.login_user, name = 'login_user'),
    path('login_page/', views.login_page, name = 'login_page'),
    path('logout_user/', views.logout_user, name = 'logout_user'),
    #path('contact_us/', views.user_msg, name = 'user_msg'),
    path('contact_us/', views.contact_us, name = 'contact_us'),
    path('msg_disp/<str:pk>', views.msg_disp, name = 'msg_disp'),
    path('capture_message/', views.capture_message, name='capture_message')
]
