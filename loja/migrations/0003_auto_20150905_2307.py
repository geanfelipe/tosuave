# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0002_auto_20150829_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='lojas',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.date(2015, 9, 5), auto_now=True, auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produtos',
            name='data_criacao',
            field=models.DateTimeField(default=datetime.date(2015, 9, 5), auto_now=True, auto_now_add=True),
            preserve_default=False,
        ),
    ]
