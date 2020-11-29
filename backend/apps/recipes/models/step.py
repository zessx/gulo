from django.db import models
from django.utils.translation import gettext as _

from apps.recipes.models import Recipe


class Step(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name='steps',
        on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(
        verbose_name=_('order')
    )
    text = models.TextField(
        verbose_name=_('text')
    )

    class Meta:
        verbose_name = _('step')
        verbose_name_plural = _('steps')

    def __str__(self):
        return _('Step %(order)d') % {'order': self.order}
