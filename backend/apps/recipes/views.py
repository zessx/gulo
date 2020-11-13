import requests
from uuid import uuid4

from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from apps.recipes.models import Recipe, Tag, Ingredient, Step
from apps.recipes.serializers import RecipeSerializer, RecipeWriteSerializer, TagSerializer, IngredientSerializer, StepSerializer

# viewsets.ModelViewSet functions to be override:
# - list()
# - retrieve()
# - create()
# - update()
# - partial_update()
# - destroy()

class RecipeViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Allows recipes to be viewed or edited.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return RecipeSerializer
        return RecipeWriteSerializer

    @action(methods=['get'], detail=False, permission_classes=[permissions.IsAuthenticated],
            url_path='tags', url_name='tags')
    def get_all_tags(self, request, pk=None):
        """
        Retrieve all tags.
        """
        queryset = Tag.objects.all()
        return Response(status=status.HTTP_200_OK, data=TagSerializer(queryset, many=True).data)

    @action(methods=['post'], detail=False, permission_classes=[permissions.IsAuthenticated],
            url_path='search', url_name='recipe_search')
    def search(self, request, pk=None):
        """
        Search recipes.
        """
        args = {}

        recipes = Recipe.objects.all()
        try:
            recipes = recipes.filter(title__icontains=request.data['text']) | recipes.filter(steps__text__icontains=request.data['text'])
        except KeyError:
            pass

        try:
            recipes = recipes.filter(tags__name=request.data['tag'])
        except KeyError:
            pass

        return Response(status=status.HTTP_200_OK, data=RecipeSerializer(recipes.distinct(), many=True).data)



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

        ingredient = Ingredient(name=request.data['name'], quantity=request.data['quantity'], unit=request.data['unit'], recipe_id=recipe.pk)
        ingredient.save()

        return Response(status=status.HTTP_200_OK, data=IngredientSerializer(ingredient).data)


class StepViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Allows recipe steps to be viewed or edited.
    """
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=kwargs['parent_lookup_recipe_id'])
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = recipe.steps.all().order_by('order')
        return Response(status=status.HTTP_200_OK, data=StepSerializer(queryset, many=True).data)

    def create(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=kwargs['parent_lookup_recipe_id'])
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)

        step = Step(text=request.data['text'], order=recipe.steps.count(), recipe_id=recipe.pk)
        step.save()

        try:
            recipe.move_step(step, request.data['order'])
        except IndexError as err:
            pass

        return Response(status=status.HTTP_200_OK, data=StepSerializer(step).data)

    def destroy(self, request, *args, **kwargs):
        recipe = Recipe.objects.get(pk=kwargs['parent_lookup_recipe_id'])
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)

        step = self.get_object()
        step.delete()

        recipe.reorder_steps()

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=['put'], detail=True, url_path='move', url_name='recipe-steps_move')
    def move(self, request, pk=None, *args, **kwargs):
        """
        Move a step.
        """
        recipe = Recipe.objects.get(pk=kwargs['parent_lookup_recipe_id'])
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)

        step = self.get_object()
        if not step:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            recipe.move_step(step, request.data['order'])
        except Step.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        except IndexError as err:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=str(err))

        return Response(status=status.HTTP_200_OK)
