# Generated by Django 5.1.4 on 2025-02-01 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0005_alter_curso_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='aulas',
            name='link',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
