# Generated by Django 5.0.2 on 2024-03-03 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_alter_recipeingredient_ingredient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='recipes',
            field=models.ManyToManyField(through='ledger.RecipeIngredient', to='ledger.recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='ledger.RecipeIngredient', to='ledger.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ledger.recipe'),
        ),
    ]
