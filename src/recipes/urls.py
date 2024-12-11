from django.urls import path
from .views import RecipeListView, RecipeDetailView, HomeView, search

app_name = "recipes"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),  # Add this line for the homepage
    path("list/", RecipeListView.as_view(), name="list"),
    path("list/<pk>", RecipeDetailView.as_view(), name="detail"),
    path("search/", search, name="search"),
]
