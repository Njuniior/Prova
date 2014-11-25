# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0010_cadastropessoa_nivelacesso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='HoraSaida',
            field=models.DateTimeField(null=True, verbose_name=b'Hora de Saida', blank=True),
        ),
    ]
