# Generated by Django 3.1.4 on 2021-02-03 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0005_species'),
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.CharField(max_length=255, verbose_name='Семейство')),
            ],
            options={
                'db_table': 'family',
            },
        ),
    ]
