from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe

# Create your views here.

# "index" view
class recipe_list(ListView):
    template_name = 'ledger/recipe_list.html' 
    context_object_name = 'recipe_container'

    def get_queryset(self):
        return Recipe.objects.all()

class recipe_detail(DetailView):
    template_name = 'ledger/recipe_detail.html'
    model = Recipe
