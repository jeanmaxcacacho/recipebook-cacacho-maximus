from django.db import models

# Create your models here.


class Ingredient(models.Model):
    name = models.charField(max_length=100)


class Recipe(models.Model):
    name = models.charField(max_length=100)


class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    # are more parameters to add????????????????
    ingredient = models.ForeignKey(
            Ingredient,
            on_delete=models.CASCADE
        )
    recipe = models.ForeignKey(
            Recipe,
            on_delete=models.CASCADE
        )
