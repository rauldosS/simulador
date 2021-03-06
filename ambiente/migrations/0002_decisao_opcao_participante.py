# Generated by Django 3.1.2 on 2020-11-07 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idade', models.IntegerField(verbose_name='Idade')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('I', 'Indefinido')], max_length=1, verbose_name='Sexo')),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambiente.ambiente')),
            ],
            options={
                'verbose_name': 'Participante',
                'verbose_name_plural': 'Participantes',
                'ordering': ('id', 'ambiente', 'nome'),
            },
        ),
        migrations.CreateModel(
            name='Opcao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opcao', models.IntegerField(verbose_name='Opcao')),
                ('direcao', models.CharField(choices=[('C', 'Cima'), ('D', 'Direita'), ('B', 'Baixo'), ('E', 'Esquerda')], max_length=1, verbose_name='Direcao')),
                ('duracao', models.IntegerField(verbose_name='Tempo em segundos')),
                ('tipo', models.CharField(choices=[('I', 'Início'), ('R', 'Rota'), ('D', 'Decisão'), ('P', 'Parada'), ('F', 'Fim')], max_length=1, verbose_name='Tipo de opção')),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambiente.ambiente')),
            ],
            options={
                'verbose_name': 'Opção',
                'verbose_name_plural': 'Opções',
                'ordering': ('id', 'opcao', 'ambiente'),
            },
        ),
        migrations.CreateModel(
            name='Decisao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('formula', models.CharField(max_length=255, verbose_name='Fórmula')),
                ('opcao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambiente.opcao')),
            ],
            options={
                'verbose_name': 'Decisão',
                'verbose_name_plural': 'Decisões',
                'ordering': ('id', 'opcao', 'formula'),
            },
        ),
    ]
