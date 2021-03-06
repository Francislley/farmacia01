# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-27 19:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('contato', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('contato', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=20)),
                ('fabricacao', models.DateField()),
                ('vencimento', models.DateField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Fornecedor')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_insercao', models.DateTimeField(auto_now=True)),
                ('cod_barra', models.IntegerField()),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento_Entrada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateTimeField(auto_now_add=True)),
                ('quantidade', models.IntegerField()),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Lote')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento_Saida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_saida', models.DateTimeField(auto_now_add=True)),
                ('quantidade', models.IntegerField()),
                ('lote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Lote')),
                ('medicamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Medicamento')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('login', models.CharField(max_length=50)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='medicamento_saida',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Usuario'),
        ),
        migrations.AddField(
            model_name='medicamento_entrada',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controle.Usuario'),
        ),
    ]
