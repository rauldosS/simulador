# Generated by Django 3.1.2 on 2020-11-22 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0023_auto_20201119_2029'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='decisao_falsa',
            field=models.CharField(default=1, max_length=255, verbose_name='Decisão Falsa'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='atividade',
            name='decisao_verdadeira',
            field=models.CharField(default=1, max_length=255, verbose_name='Decisão verdadeira'),
            preserve_default=False,
        ),
    ]
