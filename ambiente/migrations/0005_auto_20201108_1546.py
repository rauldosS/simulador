# Generated by Django 3.1.2 on 2020-11-08 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0004_auto_20201107_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='ambiente',
            name='versao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opcao',
            name='versao',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
