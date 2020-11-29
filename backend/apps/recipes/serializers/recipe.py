from rest_framework import serializers
from django.conf import settings
from django.utils.translation import ngettext

from apps.recipes.models import Recipe
from apps.recipes.serializers import TagSerializer, IngredientSerializer, StepSerializer


class RecipeSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    steps = serializers.SerializerMethodField(read_only=True)

    def get_picture(self, obj):
        return obj.picture.url if obj.picture \
            else settings.STATIC_URL + 'images/default_recipe.png'

    def get_steps(self, obj):
        steps = obj.steps.all().order_by('order')
        return StepSerializer(steps, many=True, read_only=True).data

    class Meta:
        model = Recipe
        fields = [
            'pk',
            'title',
            'picture',
            'dish',
            'duration',
            'portions',
            'tags',
            'ingredients',
            'steps'
        ]


class RecipeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'duration',
            'portions'
        ]
