# Generated by Django 3.1.2 on 2020-10-09 13:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20201008_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesjauzytkownika',
            name='id',
            field=models.UUIDField(default=uuid.UUID('62f4ad81-4242-467c-9c10-31b171645e66'), editable=False, primary_key=True, serialize=False),
        ),
    ]