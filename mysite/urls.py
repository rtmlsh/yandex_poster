from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from places import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('places.urls')),
    path('places/', include('places.urls')),
    path('', RedirectView.as_view(url='/places/', permanent=True)),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
