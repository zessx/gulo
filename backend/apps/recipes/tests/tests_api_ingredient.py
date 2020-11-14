from django.test import tag
from rest_framework import status
from rest_framework.test import APITestCase
from apps.users.models import User
from apps.recipes.models import Recipe, Ingredient

class IngredientApiTests(APITestCase):

    @tag('fast', 'api', 'ingredients')
    def test_create_with_no_unit(self):
        user = User(email='test@test.test', password='test', is_superuser=True)
        user.save()
        self.assertEqual(User.objects.count(), 1)
        self.client.force_authenticate(user=user)

        response = self.client.post('http://0.0.0.0:8000/api/recipes', {'title': 'Recipe'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Recipe.objects.count(), 1)

        response = self.client.post('http://0.0.0.0:8000/api/recipes/1/ingredients', {'name': 'Ingredient'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Ingredient.objects.count(), 1)
