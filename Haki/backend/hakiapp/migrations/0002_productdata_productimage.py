# Generated by Django 4.2.5 on 2023-09-27 17:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hakiapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdata',
            name='productImage',
            field=cloudinary.models.CloudinaryField(default='null', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
