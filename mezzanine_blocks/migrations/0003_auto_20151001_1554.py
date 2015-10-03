# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mezzanine_blocks', '0002_auto_20150719_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='mezzanine_blocks.BlockCategory', null=True),
        ),
        migrations.AlterField(
            model_name='imageblock',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='mezzanine_blocks.BlockCategory', null=True),
        ),
        migrations.AlterField(
            model_name='richblock',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='mezzanine_blocks.BlockCategory', null=True),
        ),
    ]
