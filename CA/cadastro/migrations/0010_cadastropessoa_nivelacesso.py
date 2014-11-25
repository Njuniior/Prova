# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0009_auto_20141125_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastropessoa',
            name='NivelAcesso',
            field=models.IntegerField(null=True, verbose_name=b'Nivel de Acesso', choices=[(1, b'Livre'), (2, b'Restrito'), (3, b'Reservado')]),
            preserve_default=True,
        ),
    ]
