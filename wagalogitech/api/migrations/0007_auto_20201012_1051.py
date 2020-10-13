# Generated by Django 3.1.2 on 2020-10-12 10:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201011_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pomiar',
            options={'ordering': ['stworzona'], 'verbose_name': 'Pomiar', 'verbose_name_plural': 'Pomiary'},
        ),
        migrations.AddField(
            model_name='pomiar',
            name='stworzona',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]