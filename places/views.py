from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from places.models import Place, ImagePlace


def serialize_place(place):
    serialized_place = {
        'title': place.title,
        'place_id': place.place_id,
        'short_description': place.short_description,
        'description': place.short_description,
        'longitude': place.longitude,
        'latitude': place.latitude,
        'images': [image.image.url for image in place.images.all()]
    }

    return serialized_place


def create_geojson(place):
    requested_place = serialize_place(place)
    place = {
            'type': 'Feature',
            'geometry': {'type': 'Point', 'coordinates': [requested_place['longitude'], requested_place['latitude']]},
            'properties': {'title': requested_place['title'], 'placeId': requested_place['place_id'], 'detailsUrl': 'test'}
        }

    return place


def show_event(request):
    places = Place.objects.all()
    context = {
        'place_features': {
            'type': 'FeatureCollection',
            'features': [create_geojson(place) for place in places]
        }
    }

    return render(request, "index.html", context)


def get_event(request, slug):
    place = get_object_or_404(Place, place_id=slug)
    requested_place = serialize_place(place)

    response = JsonResponse(
        {
            'title': requested_place['title'],
            'images': requested_place['images'],
            'description_short': requested_place['short_description'],
            'description_long': requested_place['description'],
            'coordinates': {
                'lng': requested_place['longitude'],
                'lat': requested_place['latitude']
            }
         },
        json_dumps_params={'ensure_ascii': False, 'indent': 2},

    )

    return HttpResponse(response.content, content_type='application/json; charset=utf-8')