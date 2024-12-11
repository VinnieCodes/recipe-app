from django.shortcuts import render  # imported by default
from django.views.generic import (
    ListView,
    DetailView,
    TemplateView,
)  # to display lists and details
from .models import Recipe  # to access Book model

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import RecipeSearchForm
from .models import Recipe
from .utils import get_recipe_name_from_id
import pandas as pd


# Create your views here.
class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = "recipes/main.html"  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):  # class-based view
    model = Recipe  # specify model
    template_name = "recipes/detail.html"  # specify template


class HomeView(TemplateView):  # Add this class for the homepage
    template_name = "recipes/home.html"


def search(request):
    form = RecipeSearchForm(request.POST or None)
    recipes_df = None
    if request.method == "POST":
        recipe_title = request.POST.get("recipe_title")
        chart_type = request.POST.get("chart_type")
        # display in terminal - needed for debugging during development only
        qs = Recipe.objects.filter(name__icontains=recipe_title)
        if qs:
            recipes_df = pd.DataFrame(qs.values())
            recipes_df["name"] = recipes_df["id"].apply(
                get_recipe_name_from_id
            )
            recipes_df["pic"] = recipes_df["pic"].apply(
                lambda x: f'<img src="{x}" width="100" height="100"/>'
            )

        recipes_df = recipes_df.to_html(escape=False)

    context = {
        "form": form,
        "recipes_df": recipes_df,
    }

    return render(request, "recipes/search.html", context)
