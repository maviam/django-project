from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all().order_by('-id')
    return render(
        request,
        'recipes/pages/home.html',
        {
            'recipes': recipes
        }
    )

def recipe(request, id_recipe):
    return render(
        request,
        'recipes/pages/recipe-view.html',
        {
            'recipe': make_recipe(),
            'is_detail_page': True
        }
    )

def category(request, category_id):
    recipes = Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id')
    return render(
        request,
        'recipes/pages/category.html',
        {
            'recipes': recipes
        }
    )
