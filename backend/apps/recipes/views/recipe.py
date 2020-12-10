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
        recipes = Recipe.objects.all()

        if 'text' in request.data:
            recipes = recipes.filter(title__icontains=request.data['text']) | \
                recipes.filter(steps__text__icontains=request.data['text']) | \
                recipes.filter(ingredients__name__icontains=request.data['text'])

        if 'tags' in request.data:
            for tag in request.data['tags']:
                recipes = recipes.filter(tags__name=tag)

        if 'dish' in request.data:
            recipes = recipes.filter(dish=request.data['dish'])

        orderbyList = ['-updated_at']
        if 'sort' in request.data:
            if request.data['sort'] in ['popular', 'popularity']:
                orderbyList = ['-popularity'] + orderbyList
            if request.data['sort'] in ['duration', 'timing']:
                orderbyList = ['duration'] + orderbyList
        recipes = recipes.order_by(*orderbyList)

        return Response(status=status.HTTP_200_OK, data=RecipeSerializer(recipes.distinct(), many=True).data)
