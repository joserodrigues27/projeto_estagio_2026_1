from django.contrib import admin
from . import models


@admin.register(models.Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'assunto', 'lido', 'data_envio')
    ordering = ('-data_envio',)
    list_editable = ('lido',)
    list_filter = ('lido', 'assunto', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    list_per_page = 10
