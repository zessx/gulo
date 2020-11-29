from rest_framework import serializers
from django.utils.translation import ngettext

from apps.recipes.models import Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    unit = serializers.SerializerMethodField(read_only=True)

    def get_unit(self, obj):
        if obj.unit == Ingredient.UNIT_PINCH:
            return ngettext('pinch', 'pinches', obj.quantity)
        elif obj.unit:
            return Ingredient.UNITS[obj.unit]
        return obj.unit

    class Meta:
        model = Ingredient
        fields = [
            'pk',
            'name',
            'quantity',
            'unit'
        ]
