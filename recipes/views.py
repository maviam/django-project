from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Page Home')

def about(request):
    return HttpResponse('Page with informations about recipes')

def contacts(request):
    return HttpResponse('Contacts Page')