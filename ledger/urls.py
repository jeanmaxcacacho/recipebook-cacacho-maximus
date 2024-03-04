from django.urls import path
from .views import *

urlpatterns = [
    path('recipes/list/', recipe_list.as_view(), name='recipe_list'),
    # path('recipe/<int:id>/', recipe_deatil.as_view(), name='recipe_detail'),
]
