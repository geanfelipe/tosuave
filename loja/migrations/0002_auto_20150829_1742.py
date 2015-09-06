# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lojas',
            name='CEP',
            field=models.CharField(default='', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lojas',
            name='numero',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
