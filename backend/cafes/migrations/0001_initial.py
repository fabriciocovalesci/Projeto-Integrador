# Generated by Django 3.0.4 on 2020-04-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cafes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('ml', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('foto_cafe', models.ImageField(blank=True, null=True, upload_to='cafes')),
            ],
            options={
                'verbose_name': 'Cafe',
                'verbose_name_plural': 'Cafes',
            },
        ),
    ]