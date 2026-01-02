from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Mensagem(models.Model):
    ASSUNTOS = {
        'desenvolvimento': 'Desenvolvimento Web/App',
        'consultoria': 'Consultoria Técnica',
        'integracao': 'Integração de Sistemas',
        'outros': 'Outros Assuntos',
    }

    nome = models.CharField(max_length=100)
    telefone = PhoneNumberField(region="BR")
    email = models.EmailField(max_length=254)
    assunto = models.CharField(max_length=50, choices=ASSUNTOS)
    mensagem = models.TextField()
    data_envio = models.DateTimeField(default=timezone.now)
    lido = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
