# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
        ('mezzanine_blocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('slug', models.CharField(help_text='Leave blank to have the URL auto-generated from the title.', max_length=2000, null=True, verbose_name='URL', blank=True)),
                ('site', models.ForeignKey(editable=False, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
        ),
        migrations.AddField(
            model_name='block',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Section', blank=True, to='mezzanine_blocks.Section', null=True),
        ),
        migrations.AddField(
            model_name='imageblock',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Section', blank=True, to='mezzanine_blocks.Section', null=True),
        ),
        migrations.AddField(
            model_name='richblock',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Section', blank=True, to='mezzanine_blocks.Section', null=True),
        ),
    ]
