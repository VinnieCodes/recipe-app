from django.shortcuts import render                     #imported by default
from django.views.generic import ListView, DetailView   #to display lists and details
from .models import Recipe                                #to access Book model

# Create your views here.
class RecipeListView(ListView):                           #class-based view
  model = Recipe                                        #specify model
  template_name = 'recipes/main.html'                   #specify template

class RecipeDetailView(DetailView):                       #class-based view
  model = Recipe                                        #specify model
  template_name = 'recipes/detail.html'                 #specify template