from django.db import models
from django.urls import reverse

# Create your models here.

"""
https://stackoverflow.com/questions/2642613/what-is-related-name-used-for
https://www.youtube.com/watch?v=qJUgC4T5e_E
"""

# only two paths in ledger.urls and max 3 templates
# we'll have og index view, list of all recipes
# then have detail view of each recipe where only list of one recipe is rendered

# done
class Ingredient(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name

# both views will use this model
# this model accesses RecipeIngredient to get recipe and the ingredients associated with that recipe
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)


    def __str__(self):
        return self.name


# this model will be the "joining table"
class RecipeIngredient(models.Model):
    quantity = models.IntegerField()
    ingredient = models.ForeignKey(  
            Ingredient,
            on_delete=models.CASCADE,
            default=1
        )
    recipe = models.ForeignKey(
            Recipe,
            on_delete=models.CASCADE,
            default=1
        )