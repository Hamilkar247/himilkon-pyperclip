# Generated by Django 3.1.2 on 2020-10-08 12:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jednostkaorganizacyjna',
            options={'verbose_name': 'Jednostka Organizacyjna', 'verbose_name_plural': 'Jednostki Organizacyjne'},
        ),
        migrations.AlterModelOptions(
            name='logadministracyjny',
            options={'verbose_name': 'Log Administracyjny', 'verbose_name_plural': 'Logi Administracyjne'},
        ),
        migrations.AlterModelOptions(
            name='logpomiarowy',
            options={'verbose_name': 'Log Pomiarowy', 'verbose_name_plural': 'Logi Pomiarowe'},
        ),
        migrations.AlterModelOptions(
            name='pomiar',
            options={'verbose_name': 'Pomiar', 'verbose_name_plural': 'Pomiary'},
        ),
        migrations.AlterModelOptions(
            name='seriapomiarowa',
            options={'verbose_name': 'Seria Pomiarowwa', 'verbose_name_plural': 'Serie Pomiarowe'},
        ),
        migrations.AlterModelOptions(
            name='sesjauzytkownika',
            options={'verbose_name': 'Sesja Użytkownika', 'verbose_name_plural': 'Sesje Użytkowników'},
        ),
        migrations.AlterModelOptions(
            name='uzytkownik',
            options={'verbose_name': 'Użytkownik', 'verbose_name_plural': 'Użytkownicy'},
        ),
        migrations.AlterField(
            model_name='sesjauzytkownika',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0985b867-53fc-47c1-91ac-7bc37c04af04'), editable=False, primary_key=True, serialize=False),
        ),
    ]
