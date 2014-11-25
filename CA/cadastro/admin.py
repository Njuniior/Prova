#coding:utf-8
from django.contrib import admin
from models import CadastroPessoa, CadastroLocal, Presenca

# Register your models here.

class CadastroPessoaAdmin (admin.ModelAdmin):
	list_display = ['Nome','Cidade','Sexo']

class CadastrolocalAdmin (admin.ModelAdmin):
	list_display = ['NomeLocal','TipoLocal']

class PresencaAdmin (admin.ModelAdmin):
	list_display = ['Nome','Local', 'HoraEntrada','HoraSaida']


admin.site.register(CadastroPessoa,CadastroPessoaAdmin)
admin.site.register(CadastroLocal,CadastrolocalAdmin)
admin.site.register(Presenca,PresencaAdmin)

