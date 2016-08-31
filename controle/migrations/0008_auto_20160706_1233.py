# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0007_auto_20160606_0222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='fornecedor',
            field=models.ForeignKey(to='controle.Fornecedor', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
