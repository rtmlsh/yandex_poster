# Generated by Django 3.2.13 on 2022-07-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_alter_imageplace_my_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Короткое описание'),
        ),
    ]
