# Generated by Django 3.1.2 on 2020-12-07 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organizacja',
            options={'ordering': ['id'], 'verbose_name': 'Organizacja', 'verbose_name_plural': 'Organizacje'},
        ),
    ]
