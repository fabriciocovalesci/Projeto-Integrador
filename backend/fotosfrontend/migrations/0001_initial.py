# Generated by Django 3.0.4 on 2020-04-08 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FotosFrontend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_frontend', models.ImageField(blank=True, null=True, upload_to='fotosfrontend')),
            ],
        ),
    ]
