# Generated by Django 3.1.2 on 2020-11-13 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0016_auto_20201111_0744'),
    ]

    operations = [
        migrations.AddField(
            model_name='predefinicaosimulacao',
            name='participante',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]