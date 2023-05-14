# Generated by Django 3.1.14 on 2023-05-14 07:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0016_auto_20230514_1133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 14, 7, 43, 25, 261613, tzinfo=utc), verbose_name='Когда появился'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 14, 17, 43, 25, 261613, tzinfo=utc), verbose_name='Когда исчезнет'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='object_pokemon', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
