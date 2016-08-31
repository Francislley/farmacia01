# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controle', '0009_auto_20160706_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamento_entrada',
            name='lote',
            field=models.ForeignKey(to='controle.Lote'),
        ),
    ]
