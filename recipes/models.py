from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=30)
    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=30)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True) # Coloca a data e hora atual e nunca mais é alterada
    updated_at = models.DateTimeField(auto_now=True) # Coloca a data e hora atual e atualiza cada vez que existe uma alteração
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/', blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, default=None) # OneToOneField (1 - 1), ForeignKey (1 - N), ManyToManyField( N - N)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.title
    
