from django.db import models
from django.urls import reverse

# Create your models here.

"""
https://stackoverflow.com/questions/2642613/what-is-related-name-used-for
https://stackoverflow.com/questions/15306897/django-reverse-lookup-of-foreign-keys?fbclid=IwAR3DA6HZVz7oJ64uu6cJGfcfX9a0y0qf52tekSvRDSl-qbHzuxkHJkSoWdg
"""

""" TODO:
    - find a way for quantity field of RecipeIngredient be accessible (ask around) __DONE__
        - last night at 2 AM I learned what reverse lookups are :)
    - populate models
        - Recipe 1
        - Recipe 2
    - make view classes
    - make templates
"""


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse(self.name, args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse(self.name, args=[str(self.name)])


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=20)
    ingredient = models.ForeignKey(  
            Ingredient,
            on_delete=models.CASCADE,
            related_name = 'ingredients' # Ingredient.ingredients accesses RecipeIngredient from Ingredient
        )
    recipe = models.ForeignKey(
            Recipe,
            on_delete=models.CASCADE,
            related_name = 'recipes' # Recipe.recipes accesses RecipeIngredient from Recipe
        )
