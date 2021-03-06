from django.db import models
from django.utils import timezone

# Create your models here.
class PredefinicaoSimulacao(models.Model):
    nome = models.CharField(max_length=255)
    participante = models.TextField()
    
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

class MapaAmbiente(models.Model):
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    versao = models.IntegerField()
    mapa = models.TextField()

    def __str__(self):
        return f'{self.id} - {self.ambiente} - {self.versao}'

    class Meta:
        verbose_name = 'Mapa ambiente'
        verbose_name_plural = 'Mapas ambientes'
        ordering = ('id', 'ambiente', 'versao')

class Atividade(models.Model):
    DIRECAO_CHOICES = (
        ('C', 'Cima'),
        ('D', 'Direita'),
        ('B', 'Baixo'),
        ('E', 'Esquerda'),
        ('F', 'Fim'),
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
    proxima_atividade = models.CharField('Próxima atividade', max_length=255, blank=True, null=True)
    atividade_anterior = models.CharField('Atividade Anterior', max_length=255, blank=True, null=True)
    decisao_verdadeira = models.CharField('Decisão verdadeira', max_length=255, blank=True, null=True)
    decisao_falsa = models.CharField('Decisão Falsa', max_length=255, blank=True, null=True)
    linha = models.CharField('linha', max_length=10)
    coluna = models.CharField('coluna', max_length=10)
    icone = models.CharField(max_length=255, blank=True, null=True)
    atividade = models.CharField('Atividade', max_length=255)
    direcao = models.CharField('Direcao', max_length=2, choices=DIRECAO_CHOICES, blank=True, null=True)
    duracao = models.IntegerField('Tempo em segundos')
    tipo = models.CharField('Tipo de opção', max_length=1, choices=TIPO_CHOICES)
    formula = models.TextField('Fórmula', blank=True, null=True)
    
    def __str__(self):
        return f'{self.id} - ({self.linha}-{self.coluna}) - {self.atividade}'

    class Meta:
        verbose_name = 'Atividade'
        verbose_name_plural = 'Atividades'
        ordering = ('id', 'linha', 'ambiente')

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
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    formula = models.CharField('Fórmula', max_length=255)

    def __str__(self):
        return f'{self.id} - {self.atividade} - {self.formula}'

    class Meta:
        verbose_name = 'Decisão'
        verbose_name_plural = 'Decisões'
        ordering = ('id', 'atividade', 'formula')