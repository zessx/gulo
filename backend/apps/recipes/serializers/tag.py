from rest_framework import serializers

from apps.recipes.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'name'
        ]
