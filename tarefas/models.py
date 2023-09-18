from django.db import models

class Tarefa(models.Model):
    titulo  = models.CharField(max_length=80, null=False, blank=False)
    dt_criacao = models.DateField(auto_now_add=True, null=False, blank=False)
    dt_prevista = models.DateField(null=False, blank=False)
    dt_conclusao = models.DateField(null=True)