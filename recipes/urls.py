from django.urls import path
from django.http import HttpResponse
from recipes.views import about, contacts, home

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contacts/', contacts)
]