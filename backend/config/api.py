from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin

from apps.users.views import UserViewSet
from apps.recipes.views import RecipeViewSet, IngredientViewSet, StepViewSet

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

# Settings
api = NestedDefaultRouter()
api.trailing_slash = '/?'

# Users API
api.register(r'users', UserViewSet)
api_recipes = api.register(r'recipes', RecipeViewSet)
api_recipes.register(r'steps', StepViewSet, basename='recipes-steps', parents_query_lookups=['recipe_id'])
api_recipes.register(r'ingredients', IngredientViewSet, basename='recipes-ingredients', parents_query_lookups=['recipe_id'])
