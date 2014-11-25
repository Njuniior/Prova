# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cadastro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('CPF', models.CharField(max_length=14, verbose_name=b'CPF')),
                ('Email', models.EmailField(max_length=75, verbose_name=b'Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
