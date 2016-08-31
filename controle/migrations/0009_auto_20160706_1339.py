# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0008_auto_20160706_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lote',
            name='fornecedor',
            field=models.ForeignKey(to='controle.Fornecedor'),
        ),
        migrations.AlterField(
            model_name='medicamento_entrada',
            name='lote',
            field=models.ForeignKey(to='controle.Lote', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
