from django.shortcuts import render
from places.models import Place, ImagePlace


def serialize_place(place):
    serialized_place = {
        "title": place.title,
        "place_id": place.place_id,
        "coordinates": {
            "lng": float(place.longitude),
            "lat": place.latitude
        }
    }
    return serialized_place


def get_event(request):
    places = Place.objects.all()
    context = {
        'place_specifies': [serialize_place(place) for place in places]
    }
    return render(request, "index.html", context)
