from django.shortcuts import render                     #imported by default
from django.views.generic import ListView, DetailView, TemplateView   #to display lists and details
from .models import Recipe                                #to access Book model

from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):                           #class-based view
  model = Recipe                                        #specify model
  template_name = 'recipes/main.html'                   #specify template

class RecipeDetailView(LoginRequiredMixin, DetailView):                       #class-based view
  model = Recipe                                        #specify model
  template_name = 'recipes/detail.html'                 #specify template

class HomeView(TemplateView):  # Add this class for the homepage
  template_name = 'recipes/home.html'