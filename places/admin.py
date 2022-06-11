from django.contrib import admin
from django.utils.html import format_html
from .models import Place, ImagePlace


class ImageInline(admin.TabularInline):
    model = ImagePlace
    fields = ('title', 'place_preview_image', 'image')
    readonly_fields = ['place_preview_image']

    def place_preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 200px;')


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]


@admin.register(ImagePlace)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['place_preview_image']

    def place_preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 200px;')
