# Generated by Django 5.1.5 on 2025-01-31 21:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cadastr',
            old_name='cidade',
            new_name='cidade_e_estado',
        ),
        migrations.RenameField(
            model_name='cadastr',
            old_name='estado',
            new_name='primeiro_e_ultimo_nome',
        ),
        migrations.RemoveField(
            model_name='cadastr',
            name='nome',
        ),
    ]
