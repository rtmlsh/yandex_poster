from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import ImagePlace, Place


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ImagePlace
    fields = ['my_order', 'title', 'place_preview_image', 'image']
    readonly_fields = ['place_preview_image']
    extra = 0

    def place_preview_image(self, obj):
        return format_html(
            '<img src={} style="max-height: 100px;/>',
            obj.image.url
        )


@admin.register(ImagePlace)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['title']
    readonly_fields = ['place_preview_image']

    def place_preview_image(self, obj):
        return format_html(
            '<img src={} style="max-height: 100px;/>',
            obj.image.url
        )


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]
