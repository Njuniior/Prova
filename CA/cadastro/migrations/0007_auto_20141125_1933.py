# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_auto_20141124_2104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Presenca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Local', models.CharField(max_length=100, null=True, verbose_name=b'Local')),
                ('HoraEntrada', models.DateTimeField(verbose_name=b'Data e Hora de Entrada')),
                ('HoraSaida', models.DateTimeField(verbose_name=b'Data e Hora de Saida')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='CPF',
            field=models.CharField(max_length=14, null=True, verbose_name=b'CPF', blank=True),
        ),
        migrations.AlterField(
            model_name='cadastrolocal',
            name='TipoLocal',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Tipo de Local', blank=True),
        ),
    ]
