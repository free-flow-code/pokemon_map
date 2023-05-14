from django.db import models  # noqa F401
from django.utils.timezone import localtime
import datetime


class Pokemon(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название на русском'
    )
    title_en = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Название на английском'
    )
    title_jp = models.CharField(
        max_length=200,
        blank=True,
        verbose_name='Название на японском'
    )
    image = models.ImageField(
        upload_to='images',
        verbose_name='Изображение'
    )
    description = models.TextField(
        blank=True,
        verbose_name='Описание'
    )
    previous_evolution = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='next_evolutions',
        verbose_name='Из кого эволюционирует'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='object_pokemon',
        verbose_name='Покемон'
    )
    Lat = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Широта'
    )
    Lon = models.FloatField(
        blank=True,
        null=True,
        verbose_name='Долгота'
    )
    appeared_at = models.DateTimeField(
        default=localtime(),
        blank=True,
        verbose_name='Когда появился'
    )
    disappeared_at = models.DateTimeField(
        default=localtime() + datetime.timedelta(minutes=600),
        blank=True,
        verbose_name='Когда исчезнет'
    )
    Level = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Уровень'
    )
    Health = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Здоровье'
    )
    Strength = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Атака'
    )
    Defence = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Защита'
    )
    Stamina = models.IntegerField(
        null=True,
        blank=True,
        verbose_name='Выносливость'
    )

    def __str__(self):
        return f'Объект {self.pokemon.title}'
