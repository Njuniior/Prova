#coding: utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES

# Create your models here.

SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')
]

class Cadastro(models.Model):
	Nome = models.CharField('Nome',max_length = 100,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	CPF = models.CharField('CPF',max_length = 14,null=True,blank=True)
	DataNascimento = models.DateField('Data de Nascimento',null=True)
	Telefone = models.CharField('Telefone',max_length=15,null=True,blank=True)
	Celular = models.CharField('Celular',max_length=15,null=True)
	Email = models.EmailField('Email',null=True)
	Endereco = models.CharField('Endereco',max_length=100,null=True)
	Complemento = models.CharField('Complemento', max_length=100,null=True,blank=True)
	Bairro = models.CharField('Bairro', max_length=100,null=True)
	Cidade = models.CharField('Cidade',max_length=100,null=True)
	UF = models.CharField('UF', max_length=2,choices=STATE_CHOICES,null=True)


	def __unicode__(self):
		return "%s - %s" % (self.id,self.Nome)

class CadastroLocal(models.Model):
	NomeLocal = models.CharField('Nome do Local',max_length = 100,null=True)
	TipoLocal = models.CharField('Tipo de Local',max_length=100,null=True,blank=True)
	

	def __unicode__(self):
		return "%s - %s" % (self.id,self.NomeLocal)




	