from django.urls import path
from . import views


urlpatterns = [
    path('', views.show_event),
    path('place/<slug:slug>', views.get_event, name='place_json')
]