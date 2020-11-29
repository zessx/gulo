# Generated by Django 3.1.2 on 2020-11-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_tag_name_unique'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='dish',
            field=models.CharField(choices=[('Starter', 'Starter'), ('Main course', 'Main course'), ('Dessert', 'Dessert')], default='Main course', max_length=50, verbose_name='Dish'),
        ),
    ]
