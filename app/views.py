from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello Django app</h1>")

def client_login(request):
    pass

def accountant_login(request):
    pass

def create_new_user(request):
    pass

def create_new_accountant(request):
    pass

def director_login(request):
    pass

def credittor_login(request):
    pass

def create_new_credittor(request):
    pass

def show_all_credits(request):
    pass

def show_credit_details(request,id):
    return HttpResponse(f"<h2>Credit sum is {id} </h2>")

def show_director_details(request):
    return HttpResponse("Director details")

def client_details(request,id):
    pass