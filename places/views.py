from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from places.models import Place, ImagePlace


def serialize_place(place):
    serialized_place = {
            'type': 'Feature',
            'geometry': {'type': 'Point', 'coordinates': [place.longitude, place.latitude]},
            'properties': {'title': place.title, 'placeId': place.place_id, 'detailsUrl': 'test'}
        }

    return serialized_place


def show_event(request):
    places = Place.objects.all()
    context = {
        'place_features': {
            'type': 'FeatureCollection',
            'features': [serialize_place(place) for place in places]
        }
    }

    return render(request, "index.html", context)


def get_event(request, slug):
    place = get_object_or_404(Place, place_id=slug)
    response = HttpResponse(place.title)
    return response