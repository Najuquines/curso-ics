# Generated by Django 5.1.4 on 2024-12-21 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dados_pessoais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
            ],
        ),
    ]