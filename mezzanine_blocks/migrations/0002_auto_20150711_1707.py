# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20150527_1555'),
        ('mezzanine_blocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='block',
            name='pages',
            field=models.ManyToManyField(to='pages.Page', blank=True),
        ),
        migrations.AddField(
            model_name='imageblock',
            name='pages',
            field=models.ManyToManyField(to='pages.Page', blank=True),
        ),
        migrations.AddField(
            model_name='richblock',
            name='pages',
            field=models.ManyToManyField(to='pages.Page', blank=True),
        ),
    ]
