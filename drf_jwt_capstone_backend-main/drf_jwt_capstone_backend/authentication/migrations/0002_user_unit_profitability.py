# Generated by Django 3.2.8 on 2021-12-04 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='unit_profitability',
            field=models.IntegerField(default=0),
        ),
    ]
