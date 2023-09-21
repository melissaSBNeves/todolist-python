from django.db import models
from datetime import date

class Tarefa(models.Model):
    titulo  = models.CharField(verbose_name="Título:",max_length=80, null=False, blank=False)
    dt_criacao = models.DateField(auto_now_add=True, null=False, blank=False)
    dt_prevista = models.DateField(verbose_name="Data de Entrega:", null=False, blank=False)
    dt_conclusao = models.DateField(null=True)

    class Meta:
        ordering = ["dt_prevista"]

    def mark_has_complete(self):
        if not self.dt_conclusao:
            self.dt_conclusao = date.today()
            self.save()