#coding:utf-8
from django.contrib import admin
from models import Presenca

# Register your models here.

class PresencaAdmin(admin.ModelAdmin):
	list_display = ['Pessoa','Local','HoraEntrada','HoraSaida']

admin.site.register(Presenca,PresencaAdmin)