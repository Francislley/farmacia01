# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0010_auto_20160706_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='numero',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='medicamento',
            name='nome',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
