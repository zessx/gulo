from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

from apps.recipes.models import Recipe


class Ingredient(models.Model):
    UNIT_CL    = 'cl'
    UNIT_L     = 'l'
    UNIT_G     = 'g'
    UNIT_KG    = 'kg'
    UNIT_TS    = 'ts'
    UNIT_TBSP  = 'tbsp'
    UNIT_PINCH = 'pinch'

    UNITS = {
        UNIT_CL:    _('cl'),
        UNIT_L:     _('l'),
        UNIT_G:     _('g'),
        UNIT_KG:    _('kg'),
        UNIT_TS:    _('tsp.'),
        UNIT_TBSP:  _('tbsp.'),
        UNIT_PINCH: _('pinch'),
    }

    recipe = models.ForeignKey(
        Recipe,
        related_name='ingredients',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name=_('name'),
        max_length=255
    )
    quantity = models.FloatField(
        verbose_name=_('quantity'),
        blank=True,
        null=True
    )
    unit = models.CharField(
        verbose_name=_('unit'),
        choices=[
            (UNIT_CL, _('cl')),
            (UNIT_L, _('l')),
            (UNIT_G, _('g')),
            (UNIT_KG, _('kg')),
            (UNIT_TS, _('tsp.')),
            (UNIT_TBSP, _('tbsp.')),
            (UNIT_PINCH, _('pinch')),
        ],
        max_length=50,
        default='',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = _('ingredient')
        verbose_name_plural = _('ingredients')

    def __str__(self):
        output = ''
        if self.quantity:
            output += str(self.quantity)
            if self.unit == self.UNIT_PINCH:
                output += ngettext('pinch', 'pinches', self.quantity) + ' '
            elif self.unit:
                output += self.UNITS[self.unit] + ' '
        output += self.name
        return output
