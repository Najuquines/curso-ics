# Generated by Django 5.1.4 on 2025-01-11 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0003_remove_aulas_cursos'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='imagem',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
