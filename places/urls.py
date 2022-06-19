from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.show_event),
    path('place/<slug:slug>', views.get_event, name='place_json'),
    path('tinymce/', include('tinymce.urls'))
]
