from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'chat' 
urlpatterns = [
    path('log_in',views.log_in, name='log_in'),
    path('log_out/',login_required(views.log_out), name='log_out'),
    path('sign_up/',views.sign_up, name='sign_up'),
    path('',login_required(views.user_list), name='user_list'),
]