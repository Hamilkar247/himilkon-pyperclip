# Generated by Django 3.1.2 on 2020-10-12 11:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201012_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pomiar',
            name='sesja_uzytkownika',
        ),
    ]
