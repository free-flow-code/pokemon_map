# Generated by Django 3.1.14 on 2023-05-14 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0020_auto_20230514_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='pokemon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pokemon_entity', to='pokemon_entities.pokemon', verbose_name='Покемон'),
        ),
    ]
