import requests
from uuid import uuid4

from django.contrib.auth import authenticate, login
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.recipes.models import Recipe, Tag, Ingredient, Step
from apps.recipes.serializers import RecipeSerializer, RecipeWriteSerializer, TagSerializer, IngredientSerializer, StepSerializer


class RecipeViewSet(viewsets.ModelViewSet):
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

    @action(methods=['get', 'post'], detail=True, permission_classes=[permissions.IsAuthenticated],
            url_path='steps', url_name='recipe_steps')
    def steps(self, request, pk=None):
        """
        Allows to get, add and delete recipe steps.
        """
        if request.method == 'POST':
            return self.add_step(request, pk=pk)
        else:
            return self.get_steps(request, pk=pk)

    def get_steps(self, request, pk=None):
        """
        Retrieve a recipe steps.
        """
        recipe = self.get_object()
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)
        queryset = recipe.steps
        return Response(status=status.HTTP_200_OK, data=StepSerializer(queryset, many=True).data)

    def add_step(self, request, pk=None):
        """
        Add a new step to a recipe.
        """
        recipe = self.get_object()
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)
        step = Step(
            order=recipe.steps.count(),
            text=request.data['text'],
            recipe_id=recipe.pk
        )
        step.save()
        return Response(status=status.HTTP_200_OK)

    @action(methods=['put'], detail=True, permission_classes=[permissions.IsAuthenticated],
            url_path='steps/move', url_name='recipe_steps_move')
    def move_step(self, request, pk=None):
        """
        Move a recipe steps.
        """
        recipe = self.get_object()
        if not recipe:
            return Response(status=status.HTTP_404_NOT_FOUND)
        try:
            step = Step.objects.get(pk=request.data['step'])
        except Step.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        order = request.data['order']
        if not (0 <= order < recipe.steps.count()):
            return Response(status=status.HTTP_400_BAD_REQUEST)

        # Update orders
        if order > step.order:
            steps_to_move = recipe.steps.filter(order__gt=step.order, order__lte=order)
            incrementer = -1
        else:
            steps_to_move = recipe.steps.filter(order__gte=order, order__lt=step.order)
            incrementer = 1

        for s in steps_to_move:
            s.order += incrementer
            s.save()

        step.order = order
        step.save()

        return Response(status=status.HTTP_200_OK)

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




class IngredientViewSet(viewsets.ModelViewSet):
    """
    Allows recipe ingredients to be viewed or edited.
    """
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticated]


class StepViewSet(viewsets.ModelViewSet):
    """
    Allows recipe steps to be viewed or edited.
    """
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    permission_classes = [permissions.IsAuthenticated]
