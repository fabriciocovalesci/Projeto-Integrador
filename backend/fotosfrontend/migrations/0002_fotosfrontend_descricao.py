# Generated by Django 3.0.4 on 2020-04-08 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fotosfrontend', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotosfrontend',
            name='descricao',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
