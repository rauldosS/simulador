# Generated by Django 3.1.2 on 2020-11-24 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0025_auto_20201122_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='formula',
            field=models.TextField(verbose_name='Fórmula'),
        ),
    ]
