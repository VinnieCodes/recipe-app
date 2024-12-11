from recipes.models import Recipe


def get_recipe_name_from_id(val):
    recipeName = Recipe.objects.get(id=val)
    return recipeName
