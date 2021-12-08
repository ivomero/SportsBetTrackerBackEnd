# Generated by Django 3.2.8 on 2021-12-07 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_game_id', models.TextField()),
                ('away_team', models.CharField(max_length=50)),
                ('home_team', models.CharField(max_length=50)),
                ('start_time', models.DateTimeField()),
                ('winner', models.CharField(max_length=1)),
            ],
        ),
    ]
