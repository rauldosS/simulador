# Generated by Django 3.1.2 on 2020-11-19 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0022_auto_20201116_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='atividade_anterior',
            field=models.CharField(max_length=255, verbose_name='Atividade Anterior'),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='proxima_atividade',
            field=models.CharField(max_length=255, verbose_name='Próxima atividade'),
        ),
    ]
