# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0002_auto_20141124_2018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cadastro',
            name='TipoDeUsuario',
        ),
        migrations.DeleteModel(
            name='TipoUsuario',
        ),
    ]
