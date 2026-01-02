from django.contrib import admin
from . import models


@admin.register(models.Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email', 'assunto', 'lida', 'data_envio')
    ordering = ('-data_envio',)
    list_editable = ('lida',)
    list_filter = ('lida', 'assunto', 'data_envio')
    search_fields = ('nome', 'email', 'mensagem')
    list_per_page = 10
