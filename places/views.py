from django.shortcuts import render
from places.models import Place, ImagePlace


def serialize_place(place):
    serialized_place = {
            'type': 'Feature',
            'geometry': {'type': 'Point', 'coordinates': [place.longitude, place.latitude]},
            'properties': {'title': place.title, 'placeId': place.place_id, 'detailsUrl': 'test'}
        }

    return serialized_place


def get_event(request):
    places = Place.objects.all()
    context = {
        'place_features': {
            'type': 'FeatureCollection',
            'features': [serialize_place(place) for place in places]
        }
    }
    return render(request, "index.html", context)
