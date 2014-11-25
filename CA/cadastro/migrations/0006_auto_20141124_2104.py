# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_auto_20141124_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastrolocal',
            name='Bairro',
        ),
        migrations.RemoveField(
            model_name='cadastrolocal',
            name='Cidade',
        ),
        migrations.RemoveField(
            model_name='cadastrolocal',
            name='Endereco',
        ),
        migrations.RemoveField(
            model_name='cadastrolocal',
            name='UF',
        ),
        migrations.AddField(
            model_name='cadastrolocal',
            name='TipoLocal',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Tipo de Local'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='Complemento',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Complemento', blank=True),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='Telefone',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Telefone', blank=True),
        ),
    ]
