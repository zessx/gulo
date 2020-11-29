from django.core.exceptions import ValidationError
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from apps.recipes.models import Recipe, Ingredient
from apps.recipes.serializers import IngredientSerializer


class IngredientViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Allows recipe ingredients to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]

    # Default create() function does not work
    # because of unrecognized recipe_id
    # No idea why.
    def create(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=kwargs['parent_lookup_recipe_id'])
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)

        args = {
            'name': request.data['name'],
            'recipe_id': recipe.pk
        }

        try:
            args['unit'] = request.data['unit']
            args['quantity'] = request.data['quantity']
        except KeyError:
            pass

        ingredient = Ingredient(**args)

        try:
            ingredient.full_clean()
        except ValidationError as err:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=err)

        ingredient.save()

        return Response(status=status.HTTP_201_CREATED, data=IngredientSerializer(ingredient).data)
