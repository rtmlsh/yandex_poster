import json
import os

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from googletrans import Translator, constants

from places.models import ImagePlace, Place


def get_json():
    files = os.listdir('json')
    for num, file in enumerate(files, 1):
        with open(f'json/{file}') as f:
            place = json.load(f)
            upload_place(place, num)


def upload_place(place, num):
    translator = Translator()
    place_id = translator.translate(place['title'], dest="en").text.split()
    new_place = Place.objects.get_or_create(
        title=place['title'],
        place_id=f'{place_id[0]}_{num}',
        short_description=place['description_short'],
        description=place['description_long'],
        longitude=place['coordinates']['lng'],
        latitude=place['coordinates']['lat']
    )
    created_place = Place.objects.get(title=place['title'])

    for url in place['imgs']:
        response = requests.get(url)
        response.raise_for_status()
        content = ContentFile(response.content)
        title = url.split('/')[-1]
        new_image = ImagePlace.objects.create(place=created_place)
        new_image.image.save(title, content, save=True)


class Command(BaseCommand):
    help = 'Автоматизированная загрузка мест в админку сайта'

    def handle(self, *args, **options):
        get_json()
