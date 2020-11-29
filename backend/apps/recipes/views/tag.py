from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from apps.recipes.models import Tag
from apps.recipes.serializers import TagSerializer


class TagViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    """
    Allows tags to be viewed or edited.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['post'], detail=False, permission_classes=[permissions.IsAuthenticated],
            url_path='search', url_name='tag_search')
    def search(self, request, pk=None):
        """
        Search tags.
        """
        args = {}

        tags = Tag.objects.all()
        try:
            tags = tags.filter(name__icontains=request.data['text'])
        except KeyError:
            pass

        return Response(status=status.HTTP_200_OK, data=TagSerializer(tags.distinct(), many=True).data)
