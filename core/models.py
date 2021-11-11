import datetime
from datetime import datetime
from _ast import mod

from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Evento(models.Model):
    objects = None
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')

    def get_data_atrasado(self):
        if self.data_evento < datetime.now():
            return True
        else:
            return False

