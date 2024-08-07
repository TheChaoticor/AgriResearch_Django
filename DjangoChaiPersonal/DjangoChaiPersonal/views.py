from django.http import HttpResponse
from django.shortcuts import render
from templates import website

def home(request):
    return HttpResponse("Hello about World")

def about(request):
    return HttpResponse("Hello about World")

def contact(request):
    return HttpResponse("Hello  contact World")