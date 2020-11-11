from django.db import models
from ambiente.models import Ambiente,  Decisao, Participante

# Create your models here.
class Cenario(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} - {self.ambiente} - {self.nome}'

    class Meta:
        verbose_name = 'Cenário'
        verbose_name_plural = 'Cenários'
        ordering = ('id', 'ambiente', 'nome')