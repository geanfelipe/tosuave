# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lojas',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=128, db_index=True)),
                ('endereco', models.CharField(max_length=256)),
                ('complemento', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Produtos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(unique=True, max_length=128, db_index=True)),
                ('quantidade', models.IntegerField()),
                ('preco', models.FloatField()),
                ('loja', models.ForeignKey(to='loja.Lojas')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
