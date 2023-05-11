from django.db import models  # noqa F401
from django.utils.timezone import localtime
import datetime


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to='images', blank=True)
    description = models.TextField(default='', blank=True)
    previous_evolution = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions'
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    Lat = models.FloatField(blank=True)
    Lon = models.FloatField(blank=True)
    appeared_at = models.DateTimeField(default=localtime(), blank=True)
    disappeared_at = models.DateTimeField(default=localtime() + datetime.timedelta(minutes=600), blank=True)
    Level = models.IntegerField(null=True, blank=True)
    Health = models.IntegerField(null=True, blank=True)
    Strength = models.IntegerField(null=True, blank=True)
    Defence = models.IntegerField(null=True, blank=True)
    Stamina = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'Объект {self.pokemon.title}'
