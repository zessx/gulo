from rest_framework import serializers

from django.conf import settings

from apps.recipes.models import Recipe, Tag, Ingredient, Step



class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = [
            'name',
            'quantity',
            'unit']


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = [
            'pk',
            'order',
            'text']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name']


class RecipeSerializer(serializers.ModelSerializer):
    picture = serializers.SerializerMethodField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    steps = serializers.SerializerMethodField(read_only=True)

    def get_picture(self, obj):
        return obj.picture.url if obj.picture else settings.STATIC_URL + \
            'images/default_recipe.png'

    def get_steps(self, obj):
        steps = obj.steps.all().order_by('order')
        return StepSerializer(steps, many=True, read_only=True).data

    class Meta:
        model = Recipe
        fields = [
            'title',
            'picture',
            'dish',
            'duration',
            'portions',
            'tags',
            'ingredients',
            'steps']


class RecipeWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'duration', 'portions']
