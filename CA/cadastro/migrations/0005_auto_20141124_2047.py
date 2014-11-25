# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_local'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Local',
            new_name='CadastroLocal',
        ),
        migrations.RemoveField(
            model_name='cadastrolocal',
            name='NomedoLocal',
        ),
        migrations.AddField(
            model_name='cadastrolocal',
            name='NomeLocal',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Nome do Local'),
            preserve_default=True,
        ),
    ]
