from django.urls import path
from recipes.views import about, contacts, home

urlpatterns = [
    path('', home),
    path('about/', about),
    path('contacts/', contacts)
]