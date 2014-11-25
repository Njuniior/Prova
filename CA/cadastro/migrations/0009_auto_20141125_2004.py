# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_auto_20141125_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='Local',
            field=models.ForeignKey(verbose_name=b'Local', to='cadastro.CadastroLocal'),
        ),
        migrations.AlterField(
            model_name='presenca',
            name='Nome',
            field=models.ForeignKey(verbose_name=b'Nome', to='cadastro.CadastroPessoa'),
        ),
    ]
