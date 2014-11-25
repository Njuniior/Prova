# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.CharField(max_length=50, null=True, verbose_name=b'Tipo de Usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='Bairro',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Bairro'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='Celular',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Celular'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='Cidade',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Cidade'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='Complemento',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Complemento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='DataNascimento',
            field=models.DateField(null=True, verbose_name=b'Data de Nascimento'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='Endereco',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Endereco'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='Sexo',
            field=models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='Telefone',
            field=models.CharField(max_length=15, null=True, verbose_name=b'Telefone'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='TipoDeUsuario',
            field=models.ForeignKey(verbose_name=b'Tipo de Usuario', to='cadastro.TipoUsuario', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cadastro',
            name='UF',
            field=models.CharField(max_length=2, null=True, verbose_name=b'UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='CPF',
            field=models.CharField(max_length=14, null=True, verbose_name=b'CPF'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='Email',
            field=models.EmailField(max_length=75, null=True, verbose_name=b'Email'),
        ),
        migrations.AlterField(
            model_name='cadastro',
            name='Nome',
            field=models.CharField(max_length=100, null=True, verbose_name=b'Nome'),
        ),
    ]
