from django.db import models
from django.utils.translation import gettext as _


class Tag(models.Model):
    name = models.CharField(
        verbose_name=_('name'),
        max_length=50,
        unique=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _('tag')
        verbose_name_plural = _('tags')

    def __str__(self):
        return self.name
