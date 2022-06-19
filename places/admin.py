from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableInlineAdminMixin, SortableAdminBase
from .models import Place, ImagePlace


class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = ImagePlace
    fields = ['my_order', 'title', 'place_preview_image', 'image']
    readonly_fields = ['place_preview_image']
    extra = 0

    def place_preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 100px;')


@admin.register(ImagePlace)
class ImageAdmin(admin.ModelAdmin):
    readonly_fields = ['place_preview_image']

    def place_preview_image(self, obj):
        return format_html(f'<img src="{obj.image.url}" style="max-height: 200px;')


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]

