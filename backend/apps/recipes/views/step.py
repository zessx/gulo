from django.core.exceptions import ValidationError
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_extensions.mixins import NestedViewSetMixin

from apps.recipes.models import Recipe, Step
from apps.recipes.serializers import StepSerializer


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

        return Response(status=status.HTTP_201_CREATED, data=StepSerializer(step).data)

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
