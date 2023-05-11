import folium
import json

from django.http import HttpResponseNotFound, HttpRequest
from django.shortcuts import render
from django.utils import timezone
from .models import PokemonEntity


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


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
    pokemons_entities = PokemonEntity.objects.filter(
        appeared_at__lt=timezone.localtime(),
        disappeared_at__gt=timezone.localtime()
    )
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in pokemons_entities:
        add_pokemon(
            folium_map, entity.Lat,
            entity.Lon,
            request.build_absolute_uri(f'../media/{entity.pokemon.image}')
        )

    pokemons_on_page = []
    for entity in pokemons_entities:
        if not entity.pokemon.image:
            pass
        pokemons_on_page.append({
            'pokemon_id': entity.pokemon.id,
            'img_url': request.build_absolute_uri(f'../media/{entity.pokemon.image}'),
            'title_ru': entity.pokemon.title,
        })
    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    timezone.activate(timezone='Europe/Moscow')
    pokemon_entities = PokemonEntity.objects.filter(
        appeared_at__lt=timezone.localtime(),
        disappeared_at__gt=timezone.localtime()
    )
    find_pokemon_entities = []
    pokemon_types = {
        '1': 'Бульбазавр',
        '2': 'Ивизавр',
        '3': 'Венузавр'
    }
    if pokemon_id in pokemon_types.keys():
        for entity in pokemon_entities:
            if entity.pokemon.title == pokemon_types[pokemon_id]:
                find_pokemon_entities.append(entity)
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for entity in find_pokemon_entities:
        add_pokemon(
            folium_map, entity.Lat,
            entity.Lon,
            request.build_absolute_uri(f'../../media/{entity.pokemon.image}')
        )
    print(find_pokemon_entities[0].pokemon.previous_evolution)
    pokemon = {
        'pokemon_id': pokemon_id,
        'img_url': request.build_absolute_uri(f'../../media/{find_pokemon_entities[0].pokemon.image}'),
        'title_ru': find_pokemon_entities[0].pokemon.title,
        'title_en': find_pokemon_entities[0].pokemon.title_en,
        'title_jp': find_pokemon_entities[0].pokemon.title_jp,
        'description': find_pokemon_entities[0].pokemon.description,
        'previous_evolution': {
            'title_ru': find_pokemon_entities[0].pokemon.previous_evolution.title,
            'pokemon_id': find_pokemon_entities[0].pokemon.previous_evolution.id,
            'img_url': request.build_absolute_uri(f'../../media/{find_pokemon_entities[0].pokemon.previous_evolution.image}')
        }
    }
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon
    })
