# Generated by Django 3.1.2 on 2020-11-17 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0020_auto_20201114_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='atividade',
            name='sequencia',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
