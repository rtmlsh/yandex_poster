from django.db import models


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название места', blank=True)
    place_id = models.CharField(max_length=200, verbose_name='Place id места', blank=True)
    short_description = models.TextField(max_length=500, verbose_name='Короткое описание', blank=True)
    description = models.TextField(verbose_name='Описание места', blank=True)
    longitude = models.FloatField(verbose_name='Долгота', null=True)
    latitude = models.FloatField(verbose_name='Широта', null=True)

    def __str__(self):
        return f'{self.title}'


class ImagePlace(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название изображения', blank=True)
    image = models.ImageField(verbose_name='Изображение', null=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images', null=True, verbose_name='Место')
    my_order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['my_order']

    def __str__(self):
        return f'{self.title}'