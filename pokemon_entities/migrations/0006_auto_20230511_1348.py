# Generated by Django 3.1.14 on 2023-05-11 09:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0005_auto_20230509_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='description',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 11, 9, 48, 10, 848115, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 11, 19, 48, 10, 848115, tzinfo=utc)),
        ),
    ]
