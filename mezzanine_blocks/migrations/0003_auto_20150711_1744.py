# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_blocks', '0002_auto_20150711_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Reihenfolge'),
        ),
        migrations.AddField(
            model_name='imageblock',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Reihenfolge'),
        ),
        migrations.AddField(
            model_name='richblock',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Reihenfolge'),
        ),
    ]
