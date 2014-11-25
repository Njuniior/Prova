# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0007_auto_20141125_1933'),
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroPessoa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nome', models.CharField(max_length=100, null=True, verbose_name=b'Nome')),
                ('Sexo', models.CharField(max_length=1, null=True, verbose_name=b'Sexo', choices=[(b'M', b'Masculino'), (b'F', b'Feminino')])),
                ('CPF', models.CharField(max_length=14, null=True, verbose_name=b'CPF', blank=True)),
                ('DataNascimento', models.DateField(null=True, verbose_name=b'Data de Nascimento')),
                ('Telefone', models.CharField(max_length=15, null=True, verbose_name=b'Telefone', blank=True)),
                ('Celular', models.CharField(max_length=15, null=True, verbose_name=b'Celular')),
                ('Email', models.EmailField(max_length=75, null=True, verbose_name=b'Email')),
                ('Endereco', models.CharField(max_length=100, null=True, verbose_name=b'Endereco')),
                ('Complemento', models.CharField(max_length=100, null=True, verbose_name=b'Complemento', blank=True)),
                ('Bairro', models.CharField(max_length=100, null=True, verbose_name=b'Bairro')),
                ('Cidade', models.CharField(max_length=100, null=True, verbose_name=b'Cidade')),
                ('UF', models.CharField(max_length=2, null=True, verbose_name=b'UF', choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amap\xe1'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Cear\xe1'), ('DF', 'Distrito Federal'), ('ES', 'Esp\xedrito Santo'), ('GO', 'Goi\xe1s'), ('MA', 'Maranh\xe3o'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Par\xe1'), ('PB', 'Para\xedba'), ('PR', 'Paran\xe1'), ('PE', 'Pernambuco'), ('PI', 'Piau\xed'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rond\xf4nia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'S\xe3o Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='Cadastro',
        ),
        migrations.AddField(
            model_name='cadastrolocal',
            name='NivelAcesso',
            field=models.IntegerField(null=True, verbose_name=b'Nivel de Acesso', choices=[(1, b'Livre'), (2, b'Restrito'), (3, b'Reservado')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='presenca',
            name='HoraEntrada',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='presenca',
            name='HoraSaida',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
