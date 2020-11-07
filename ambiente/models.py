from django.db import models
from django.utils import timezone

# Create your models here.
class Ambiente(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateField('Data de criação', auto_now=False, default=timezone.now)

    def __str__(self):
        return f'{self.id} - {self.nome} - {self.data}'

    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'
        ordering = ('id', 'nome', 'data')