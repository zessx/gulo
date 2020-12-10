# Generated by Django 3.1.2 on 2020-12-09 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_choices_keys'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='unit',
            field=models.CharField(blank=True, choices=[('cl', 'cl'), ('l', 'l'), ('g', 'g'), ('kg', 'kg'), ('tsp', 'tsp'), ('tbs', 'Tbs.'), ('pinch', 'pinch'), ('cup', 'cup')], default='', max_length=50, null=True, verbose_name='unit'),
        ),
    ]
