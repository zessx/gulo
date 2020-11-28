from django.db import models
from django.utils.translation import gettext as _
from django.utils.translation import ngettext

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


class Recipe(models.Model):
    DISH_STARTER     = 'starter'
    DISH_MAIN_COURSE = 'main_course'
    DISH_DESSERT     = 'dessert'

    DISHES = {
        DISH_STARTER:     _('Starter'),
        DISH_MAIN_COURSE: _('Main course'),
        DISH_DESSERT:     _('Dessert'),
    }

    title = models.CharField(
        verbose_name=_('title'),
        max_length=255
    )
    picture = models.ImageField(
        verbose_name=_('picture'),
        blank=True,
        null=True
    )
    dish = models.CharField(
        verbose_name=_('dish'),
        choices=[
            (DISH_STARTER, _('Starter')),
            (DISH_MAIN_COURSE, _('Main course')),
            (DISH_DESSERT, _('Dessert')),
        ],
        max_length=50,
        default=DISH_MAIN_COURSE
    )
    duration = models.CharField(
        verbose_name=_('duration'),
        max_length=255,
        blank=True,
        null=True
    )
    portions = models.CharField(
        verbose_name=_('portions'),
        max_length=255,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        Tag
    )

    class Meta:
        verbose_name = _('recipe')
        verbose_name_plural = _('recipes')

    def __str__(self):
        return self.title

    def move_step(self, step, order: int):
        """
        Move a steps, and update all other steps order
        """
        order = int(order)
        if not isinstance(step, Step):
            raise TypeError(_('Step must be an instance of Step.'))
        if not (0 <= order < self.steps.count()):
            raise IndexError(_('Order is out of range.'))

        if order > step.order:
            steps_to_move = self.steps.filter(order__gt=step.order, order__lte=order)
            incrementer = -1
        else:
            steps_to_move = self.steps.filter(order__gte=order, order__lt=step.order)
            incrementer = 1

        for s in steps_to_move:
            s.order += incrementer
            s.save()

        step.order = order
        step.save()

    def reorder_steps(self):
        """
        Call this function after deleting a step, to fill missing orders
        """
        order = 0
        for step in self.steps.all():
            step.order = order
            step.save()
            order += 1


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
