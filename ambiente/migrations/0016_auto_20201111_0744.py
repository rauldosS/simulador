# Generated by Django 3.1.2 on 2020-11-11 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0015_auto_20201111_0744'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='atividade',
            options={'ordering': ('id', 'linha', 'ambiente'), 'verbose_name': 'Atividade', 'verbose_name_plural': 'Atividades'},
        ),
    ]
