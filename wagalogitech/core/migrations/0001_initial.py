# Generated by Django 3.1.2 on 2020-11-03 12:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizacja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=200, verbose_name='Nazwa')),
                ('opis', models.CharField(max_length=500, verbose_name='Opis')),
            ],
            options={
                'verbose_name': 'Organizacja',
                'verbose_name_plural': 'Organizacje',
                'ordering': ['nazwa'],
            },
        ),
        migrations.CreateModel(
            name='SesjaUzytkownika',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_sesji', models.DateTimeField(verbose_name='start sesji')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sesjeuzytkownika', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Sesja Użytkownika',
                'verbose_name_plural': 'Sesje Użytkowników',
                'ordering': ['start_sesji'],
            },
        ),
        migrations.CreateModel(
            name='SeriaPomiarowa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa_sesji', models.CharField(max_length=100, verbose_name='nazwa sesji')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seriepomiarowe', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Seria Pomiarowwa',
                'verbose_name_plural': 'Serie Pomiarowe',
            },
        ),
        migrations.CreateModel(
            name='Pomiar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czyWazny', models.BooleanField(verbose_name='Czy ważny?')),
                ('wartosc', models.CharField(max_length=300, verbose_name='wartość')),
                ('data_pomiaru', models.DateTimeField(auto_now_add=True, verbose_name='data pomiaru')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pomiary', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pomiar',
                'verbose_name_plural': 'Pomiary',
                'ordering': ['data_pomiaru'],
            },
        ),
        migrations.CreateModel(
            name='LogPomiarowy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=500, verbose_name='Opis')),
                ('data', models.DateField(verbose_name='data')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logipomiarowe', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Log Pomiarowy',
                'verbose_name_plural': 'Logi Pomiarowe',
            },
        ),
        migrations.CreateModel(
            name='LogAdministracyjny',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opis', models.CharField(max_length=500, verbose_name='Opis')),
                ('data', models.DateField(verbose_name='Data')),
                ('czynnosc', models.CharField(max_length=200, verbose_name='Czynność')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='logiadministracyjne', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Log Administracyjny',
                'verbose_name_plural': 'Logi Administracyjne',
                'ordering': ['data'],
            },
        ),
    ]