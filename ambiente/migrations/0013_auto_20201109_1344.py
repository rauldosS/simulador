# Generated by Django 3.1.2 on 2020-11-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0012_auto_20201109_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opcao',
            name='icone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
