# Generated by Django 3.1.2 on 2020-11-09 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0009_ambiente_predefinicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcao',
            name='tipo',
            field=models.CharField(choices=[('I', 'Início'), ('R', 'Rota'), ('D', 'Decisão'), ('P', 'Parada'), ('F', 'Fim'), ('O', 'Objeto')], max_length=1, verbose_name='Tipo de opção'),
        ),
    ]
