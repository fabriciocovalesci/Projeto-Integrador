# Generated by Django 3.0.4 on 2020-04-06 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafes',
            name='foto_cafe',
            field=models.ImageField(blank=True, null=True, upload_to='cafes'),
        ),
    ]
