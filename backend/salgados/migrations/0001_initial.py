# Generated by Django 3.0.4 on 2020-04-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salgados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('unidades', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('foto_salgados', models.ImageField(blank=True, null=True, upload_to='salgados')),
            ],
            options={
                'verbose_name': 'Salgado',
                'verbose_name_plural': 'Salgados',
            },
        ),
    ]