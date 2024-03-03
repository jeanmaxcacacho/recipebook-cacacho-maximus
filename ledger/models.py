from django.db import models
from django.urls import reverse

# Create your models here.


class Ingredient(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

    
    def get_absolute_url(self): # url to what?
        return reverse('', args=[str(self.name)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('', args=[str(self.name)])


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(  # are there more parameters to add?; idt related_name is relevant since there are no "types" of connected classes
            Ingredient,
            on_delete=models.CASCADE,
            default=1
        )
    recipe = models.ForeignKey(
            Recipe,
            on_delete=models.CASCADE,
            default=1
        )
