from rest_framework import serializers

from apps.recipes.models import Step


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = [
            'pk',
            'order',
            'text'
        ]
