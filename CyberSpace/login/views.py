from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def login(request):
    return HttpResponse("Login.")

def signup(request):
    return HttpResponse("signup.")