from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from apps.recipes.models import Recipe, Tag
from apps.recipes.serializers import RecipeSerializer, RecipeWriteSerializer


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

    @action(methods=['post'], detail=False, permission_classes=[permissions.IsAuthenticated],
            url_path='search', url_name='recipe_search')
    def search(self, request, pk=None, parent_lookup_recipe=None):
        """
        Search recipes.
        """
        args = {}

        recipes = Recipe.objects.all()
        try:
            recipes = recipes.filter(title__icontains=request.data['text']) | \
                recipes.filter(steps__text__icontains=request.data['text']) | \
                recipes.filter(ingredients__name__icontains=request.data['text'])
        except KeyError:
            pass

        try:
            recipes = recipes.filter(tags__name=request.data['tag'])
        except KeyError:
            pass

        return Response(status=status.HTTP_200_OK, data=RecipeSerializer(recipes.distinct(), many=True).data)
