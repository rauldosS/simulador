from django.db import models
from django.utils import timezone

# Create your models here.
class PredefinicaoSimulacao(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.id} - {self.nome}'

    class Meta:
        verbose_name = 'Predefinição de simulação'
        verbose_name_plural = 'Predefinicações de simulações'
        ordering = ('id', 'nome')

class Ambiente(models.Model):
    nome = models.CharField(max_length=255)
    versao = models.IntegerField()
    data = models.DateField('Data de criação', auto_now=False, default=timezone.now)
    predefinicao = models.ForeignKey(PredefinicaoSimulacao, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.id} - {self.nome} - {self.data}'

    class Meta:
        verbose_name = 'Ambiente'
        verbose_name_plural = 'Ambientes'
        ordering = ('id', 'nome', 'data')

class Opcao(models.Model):
    DIRECAO_CHOICES = (
        ('C', 'Cima'),
        ('D', 'Direita'),
        ('B', 'Baixo'),
        ('E', 'Esquerda'),
        ('DC', 'Decisão'),
    )

    TIPO_CHOICES = (
        ('I', 'Início'),
        ('R', 'Rota'),
        ('D', 'Decisão'),
        ('P', 'Parada'),
        ('F', 'Fim'),
        ('O', 'Objeto')
    )

    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    versao = models.IntegerField()
    opcao = models.CharField('Opção', max_length=10)
    icone = models.CharField(max_length=255, blank=True, null=True)
    nome = models.CharField('Nome', max_length=255)
    direcao = models.CharField('Direcao', max_length=2, choices=DIRECAO_CHOICES, blank=True, null=True)
    duracao = models.IntegerField('Tempo em segundos')
    tipo = models.CharField('Tipo de opção', max_length=1, choices=TIPO_CHOICES)
    formula = models.CharField('Fórmula', max_length=1000)
    
    def __str__(self):
        return f'{self.id} - {self.opcao} - {self.nome}'

    class Meta:
        verbose_name = 'Opção'
        verbose_name_plural = 'Opções'
        ordering = ('id', 'opcao', 'ambiente')

class Participante(models.Model):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('I', 'Indefinido'),
    )

    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    nome = models.CharField('Nome', max_length=255)
    dados = models.TextField()

    def __str__(self):
        return f'{self.id} - {self.ambiente} - {self.nome}'

    class Meta:
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'
        ordering = ('id', 'ambiente', 'nome')


class Decisao(models.Model):
    opcao = models.ForeignKey(Opcao, on_delete=models.CASCADE)
    formula = models.CharField('Fórmula', max_length=255)

    def __str__(self):
        return f'{self.id} - {self.opcao} - {self.formula}'

    class Meta:
        verbose_name = 'Decisão'
        verbose_name_plural = 'Decisões'
        ordering = ('id', 'opcao', 'formula')