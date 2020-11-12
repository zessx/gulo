from django.db import models


class Tag(models.Model):
    name = models.CharField(
        verbose_name='Name',
        max_length=50,
        unique=True
    )

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Recipe(models.Model):
    DISH_STARTER = 'Starter'
    DISH_MAIN_COURSE = 'Main course'
    DISH_DESSERT = 'Dessert'

    DISH_CHOICES = [
        (DISH_STARTER, DISH_STARTER),
        (DISH_MAIN_COURSE, DISH_MAIN_COURSE),
        (DISH_DESSERT, DISH_DESSERT),
    ]

    title = models.CharField(
        verbose_name='Title',
        max_length=255
    )
    picture = models.ImageField(
        verbose_name='Picture',
        blank=True
    )
    dish = models.CharField(
        verbose_name='Dish',
        choices=DISH_CHOICES,
        max_length=50,
        default=DISH_MAIN_COURSE
    )
    duration = models.CharField(
        verbose_name='Duration',
        max_length=255,
        blank=True
    )
    portions = models.CharField(
        verbose_name='Portions',
        max_length=255,
        blank=True
    )
    tags = models.ManyToManyField(
        Tag
    )

    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    UNIT_CL = 'cl'
    UNIT_L = 'l'
    UNIT_G = 'g'
    UNIT_KG = 'kg'
    UNIT_TS = 'tsp.'
    UNIT_TBSP = 'tbsp.'
    UNIT_PINCH = 'pinch'

    UNIT_CHOICES = [
        (UNIT_CL, UNIT_CL),
        (UNIT_L, UNIT_L),
        (UNIT_G, UNIT_G),
        (UNIT_KG, UNIT_KG),
        (UNIT_TS, UNIT_TS),
        (UNIT_TBSP, UNIT_TBSP),
        (UNIT_PINCH, UNIT_PINCH),
    ]

    recipe = models.ForeignKey(
        Recipe,
        related_name='ingredients',
        on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=255
    )
    quantity = models.FloatField(
        verbose_name='Quantity',
        blank=True
    )
    unit = models.CharField(
        verbose_name='Unit',
        choices=UNIT_CHOICES,
        max_length=50,
        blank=True
    )

    class Meta:
        verbose_name = 'Ingredient'
        verbose_name_plural = 'Ingredients'

    def __str__(self):
        output  = self.quantity + ' ' if self.quantity else ''
        output += self.unit + ' ' if self.unit else ''
        output += self.name
        return output


class Step(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        related_name='steps',
        on_delete=models.CASCADE
    )
    order = models.PositiveIntegerField(
        verbose_name='Order'
    )
    text = models.TextField(
        verbose_name='Text'
    )

    class Meta:
        verbose_name = 'Step'
        verbose_name_plural = 'Steps'

    def __str__(self):
        return 'Step {}'.format(self.order)
