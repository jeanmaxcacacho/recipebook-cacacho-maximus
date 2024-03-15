from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse(self.name, args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='authored', # future use-cases of this would be to show recipes author as authored so this rel_name makes sense to me
                               null=True) 
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)
    


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


    def __str__(self):
        return f"{self.recipe} -- {self.ingredient} -- {self.quantity}"
