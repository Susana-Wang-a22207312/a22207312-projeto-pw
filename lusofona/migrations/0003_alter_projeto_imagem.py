# Generated by Django 4.0.6 on 2024-04-16 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lusofona', '0002_alter_disciplina_ano_alter_disciplina_ects_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='imagem',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]