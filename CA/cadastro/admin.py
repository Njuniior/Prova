#coding: utf-8
from django.contrib import admin
from models import Cadastro, CadastroLocal

# Register your models here.

class CadastroAdmin (admin.ModelAdmin):
	list_display = ['Nome','CPF','Cidade','Sexo']

class CadastrolocalAdmin (admin.ModelAdmin):
	list_display = ['NomeLocal','TipoLocal']


admin.site.register(Cadastro,CadastroAdmin)
admin.site.register(CadastroLocal,CadastrolocalAdmin)

