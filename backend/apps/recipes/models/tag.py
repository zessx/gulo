from django.db import models
from django.utils.translation import gettext as _


class Tag(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.name
