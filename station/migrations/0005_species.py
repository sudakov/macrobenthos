# Generated by Django 3.1.4 on 2021-01-19 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0004_auto_20210118_1342'),
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('genus_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Родовое название')),
                ('species_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Видовое название')),
                ('author', models.CharField(blank=True, max_length=50, null=True, verbose_name='Автор')),
                ('family', models.CharField(blank=True, max_length=255, null=True, verbose_name='Семейство')),
                ('remark', models.CharField(blank=True, max_length=150, null=True, verbose_name='Примечание')),
            ],
            options={
                'db_table': 'species'
            },
        ),
    ]
