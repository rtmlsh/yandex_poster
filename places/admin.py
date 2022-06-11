from django.contrib import admin
from .models import Place, ImagePlace


class ImageInline(admin.TabularInline):
    model = ImagePlace


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


admin.site.register(ImagePlace)