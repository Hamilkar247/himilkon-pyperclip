# Generated by Django 3.1.2 on 2020-10-09 13:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20201009_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sesjauzytkownika',
            name='id',
            field=models.UUIDField(default=uuid.UUID('33be1485-4e2d-479d-a722-d92cb8f15fdd'), editable=False, primary_key=True, serialize=False),
        ),
    ]