import folium
import json

from django.http import HttpResponseNotFound, HttpRequest
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import PokemonEntity, Pokemon


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def get_pokemon_image(request, pokemon_entity):
    if not pokemon_entity.pokemon.image:
        return DEFAULT_IMAGE_URL
    return request.build_absolute_uri(pokemon_entity.pokemon.image.url)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    timezone.activate(timezone='Europe/Moscow')
    time_now = timezone.localtime()
    pokemons_entities = PokemonEntity.objects.filter(
        appeared_at__lt=time_now,
        disappeared_at__gt=time_now
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in pokemons_entities:
        add_pokemon(
            folium_map, entity.lat,
            entity.lon,
            request.build_absolute_uri(entity.pokemon.image.url)
        )

    pokemons_on_page = []
    for entity in pokemons_entities:
        pokemons_on_page.append({
            'pokemon_id': entity.pokemon.id,
            'img_url': get_pokemon_image(request, entity),
            'title_ru': entity.pokemon.title,
        })
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    timezone.activate(timezone='Europe/Moscow')
    pokemon_type = get_object_or_404(Pokemon, id=int(pokemon_id))
    time_now = timezone.localtime()
    pokemon_entities = PokemonEntity.objects.filter(
        pokemon=pokemon_type,
        appeared_at__lt=time_now,
        disappeared_at__gt=time_now
    )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in pokemon_entities:
        add_pokemon(
            folium_map, entity.lat,
            entity.lon,
            request.build_absolute_uri(entity.pokemon.image.url)
        )
    pokemon = {
        'pokemon_id': pokemon_id,
        'img_url': request.build_absolute_uri(pokemon_type.image.url),
        'title_ru': pokemon_type.title,
        'title_en': pokemon_type.title_en,
        'title_jp': pokemon_type.title_jp,
        'description': pokemon_type.description,
        }
    previous_evolution_pokemon = pokemon_type.previous_evolution
    if previous_evolution_pokemon:
        pokemon['previous_evolution'] = {
            'title_ru': previous_evolution_pokemon.title,
            'pokemon_id': previous_evolution_pokemon.id,
            'img_url': request.build_absolute_uri(previous_evolution_pokemon.image.url)
            }

    next_evolution_pokemon = pokemon_type.next_evolutions.first()
    if next_evolution_pokemon:
        pokemon['next_evolution'] = {
            'title_ru': next_evolution_pokemon.title,
            'pokemon_id': next_evolution_pokemon.id,
            'img_url': request.build_absolute_uri(next_evolution_pokemon.image.url)
        }
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
