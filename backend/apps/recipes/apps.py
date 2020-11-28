from django.apps import AppConfig
from django.utils.translation import gettext as _

class RecipesConfig(AppConfig):
    name = 'apps.recipes'
    verbose_name = _('recipes')
