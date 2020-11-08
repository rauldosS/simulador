# Generated by Django 3.1.2 on 2020-11-07 00:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ambiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data', models.DateField(default=django.utils.timezone.now, verbose_name='Data de criação')),
            ],
            options={
                'verbose_name': 'Ambiente',
                'verbose_name_plural': 'Ambientes',
                'ordering': ('id', 'nome', 'data'),
            },
        ),
    ]