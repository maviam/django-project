from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
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
    recipe = get_object_or_404(Recipe.objects.filter(pk=id_recipe))
    return render(
        request,
        'recipes/pages/recipe-view.html',
        {
            'recipe': recipe,
            'is_detail_page': True
        }
    )

def category(request, category_id):
    recipes = get_list_or_404(Recipe.objects.filter(category__id=category_id, is_published=True).order_by('-id'))
    category = recipes[0].category.name
    
    return render(
        request,
        'recipes/pages/category.html',
        {
            'recipes': recipes,
            'category': category
        }
    )
