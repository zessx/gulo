from django.test import TestCase, tag

from django.core.exceptions import ValidationError

from apps.recipes.models import Recipe, Ingredient

class IngredientModelTests(TestCase):

    @tag('fast', 'ingredients', 'validators')
    def test_was_created_with_known_unit(self):
        try:
            r = Recipe(title='Recipe')
            r.save()
            i = Ingredient(recipe=r, name='Ingredient', unit=Ingredient.UNIT_CL)
            i.full_clean()
        except ValidationError as err:
            self.assertFalse('is not a valid choice' in err)
            pass

    @tag('fast', 'ingredients', 'validators')
    def test_was_created_with_unknown_unit(self):
        try:
            r = Recipe(title='Recipe')
            r.save()
            i = Ingredient(recipe=r, name='Ingredient', unit='unknown unit')
            i.full_clean()
            self.fail()
        except ValidationError as err:
            pass
