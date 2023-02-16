from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index),
    path('login/user',client_login),
    path('login/accountant',accountant_login),
    path('sign_up/user',create_new_user),
    path('sign_up/acocuntant',create_new_accountant),
    path('login/director',director_login),
    path('login/credittor',credittor_login),
    path('sign_up/credittor',create_new_credittor),
    path('credits/',show_all_credits),
    path('credits/<id>',show_credit_details),
    path('profile/director',show_director_details),
    path('client/<id>',client_details)
]