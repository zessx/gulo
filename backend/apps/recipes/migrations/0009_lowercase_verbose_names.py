# Generated by Django 3.1.2 on 2020-11-28 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_blankable_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'ingredient', 'verbose_name_plural': 'ingredients'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'verbose_name': 'recipe', 'verbose_name_plural': 'recipes'},
        ),
        migrations.AlterModelOptions(
            name='step',
            options={'verbose_name': 'step', 'verbose_name_plural': 'steps'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'tag', 'verbose_name_plural': 'tags'},
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=255, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.FloatField(blank=True, null=True, verbose_name='quantity'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, choices=[('cl', 'cl'), ('l', 'l'), ('g', 'g'), ('kg', 'kg'), ('tsp.', 'tsp.'), ('tbsp.', 'tbsp.'), ('pinch', 'pinch')], default='', max_length=50, null=True, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='dish',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Main course', 'Main course'), ('Dessert', 'Dessert')], default='Main course', max_length=50, verbose_name='dish'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='duration',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='duration'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='picture'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='portions',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='portions'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.CharField(max_length=255, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='step',
            name='order',
            field=models.PositiveIntegerField(verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='step',
            name='text',
            field=models.TextField(verbose_name='text'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='name'),
        ),
    ]
