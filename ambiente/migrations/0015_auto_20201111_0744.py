# Generated by Django 3.1.2 on 2020-11-11 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ambiente', '0014_auto_20201109_1830'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versao', models.IntegerField()),
                ('linha', models.CharField(max_length=10, verbose_name='linha')),
                ('coluna', models.CharField(max_length=10, verbose_name='coluna')),
                ('icone', models.CharField(blank=True, max_length=255, null=True)),
                ('atividade', models.CharField(max_length=255, verbose_name='Nome')),
                ('direcao', models.CharField(blank=True, choices=[('C', 'Cima'), ('D', 'Direita'), ('B', 'Baixo'), ('E', 'Esquerda'), ('DC', 'Decisão')], max_length=2, null=True, verbose_name='Direcao')),
                ('duracao', models.IntegerField(verbose_name='Tempo em segundos')),
                ('tipo', models.CharField(choices=[('I', 'Início'), ('R', 'Rota'), ('D', 'Decisão'), ('P', 'Parada'), ('F', 'Fim'), ('O', 'Objeto')], max_length=1, verbose_name='Tipo de opção')),
                ('formula', models.CharField(max_length=1000, verbose_name='Fórmula')),
                ('ambiente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ambiente.ambiente')),
            ],
            options={
                'verbose_name': 'Opção',
                'verbose_name_plural': 'Opções',
                'ordering': ('id', 'linha', 'ambiente'),
            },
        ),
        migrations.AlterModelOptions(
            name='decisao',
            options={'ordering': ('id', 'atividade', 'formula'), 'verbose_name': 'Decisão', 'verbose_name_plural': 'Decisões'},
        ),
        migrations.RemoveField(
            model_name='decisao',
            name='opcao',
        ),
        migrations.DeleteModel(
            name='Opcao',
        ),
        migrations.AddField(
            model_name='decisao',
            name='atividade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ambiente.atividade'),
            preserve_default=False,
        ),
    ]