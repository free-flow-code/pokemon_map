# Generated by Django 3.1.14 on 2023-05-14 07:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0013_auto_20230514_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 14, 7, 27, 29, 96924, tzinfo=utc), verbose_name='Когда появился'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 14, 17, 27, 29, 96924, tzinfo=utc), verbose_name='Когда исчезнет'),
        ),
    ]
