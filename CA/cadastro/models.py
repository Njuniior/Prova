#coding:utf-8
from django.db import models
from localflavor.br.br_states import STATE_CHOICES
from django.core.exceptions import ValidationError

# Create your models here.

SEXO_OPCOES = [

	('M','Masculino'),
	('F','Feminino')
]

NIVEL_OPCOES = [
(1,'Livre'),
(2,'Restrito'),
(3,'Reservado')
]

class CadastroPessoa(models.Model):
	Nome = models.CharField('Nome',max_length = 100,null=True)
	Sexo = models.CharField('Sexo',max_length=1,choices=SEXO_OPCOES,null=True)
	NivelAcesso = models.IntegerField('Nivel de Acesso',choices=NIVEL_OPCOES,null=True)
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
		return self.Nome

class CadastroLocal(models.Model):
	NomeLocal = models.CharField('Nome do Local',max_length = 100,null=True)
	TipoLocal = models.CharField('Tipo de Local',max_length=100,null=True,blank=True)
	NivelAcesso = models.IntegerField('Nivel de Acesso',choices=NIVEL_OPCOES,null=True)
	

	def __unicode__(self):
		return "%s - %s - %s" % (self.NomeLocal, self.TipoLocal, self.NivelAcesso)



class Presenca(models.Model):
	Nome = models.ForeignKey(CadastroPessoa,verbose_name='Nome')
	Local = models.ForeignKey(CadastroLocal,verbose_name='Local')
	HoraEntrada = models.DateTimeField(auto_now=True,null=True)
	HoraSaida = models.DateTimeField('Hora de Saida',blank=True,null=True)


	def __unicode__(self):
		return "%s - %s" % (self.Nome, self.Local)

	def clean(self):
		p = Presenca.objects.filter(Nome=self.Nome,HoraSaida__isnull=True)
		if p and self.id == None:
			raise ValidationError ("Usuario esta Presente em outro Local")

		if self.Local.NivelAcesso > self.Nome.NivelAcesso:
			raise ValidationError ("Usuario sem Permissão de acesso")