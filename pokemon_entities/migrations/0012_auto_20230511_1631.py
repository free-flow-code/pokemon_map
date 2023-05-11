# Generated by Django 3.1.14 on 2023-05-11 12:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0011_auto_20230511_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image',
            field=models.ImageField(upload_to='images', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Lat',
            field=models.FloatField(blank=True, null=True, verbose_name='Широта'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='Lon',
            field=models.FloatField(blank=True, null=True, verbose_name='Долгота'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 11, 12, 31, 1, 725977, tzinfo=utc), verbose_name='Когда появился'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 11, 22, 31, 1, 725977, tzinfo=utc), verbose_name='Когда исчезнет'),
        ),
    ]
