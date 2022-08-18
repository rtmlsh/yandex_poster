from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Название места', blank=True
    )
    short_description = models.TextField(
        verbose_name='Короткое описание', blank=True
    )
    description = HTMLField(blank=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True)
    latitude = models.FloatField(verbose_name='Широта', null=True)

    def __str__(self):
        return self.title


class ImagePlace(models.Model):
    title = models.CharField(
        max_length=200, verbose_name='Название изображения', blank=True
    )
    image = models.ImageField(verbose_name='Изображение', null=True)
    place = models.ForeignKey(
        Place,
        on_delete=models.CASCADE,
        related_name='images',
        null=True,
        verbose_name='Место'
    )
    order = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
