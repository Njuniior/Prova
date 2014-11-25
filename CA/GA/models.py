#coding:utf-8
from django.db import models
from Cadastro.models import Cadastro
from Cadastro.models import CadastroLocal
# Create your models here.

class Presenca(models.Model):
	Pessoa = models.CharField('Pessoa',max_length=100,null=True)
	Local = models.CharField('local',max_length=100,null=True)
	HoraEntrada = models.DateTimeField("Data e Hora Entrada")
	HoraSaida = models.DateTimeField("Data e Hora Saida")

    def __unicode__(self):
    	return "%s - %s" % (self.Pessoa,self.Local)
      
