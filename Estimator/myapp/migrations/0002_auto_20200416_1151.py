# Generated by Django 3.0 on 2020-04-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covid19',
            name='avgDailyIncomeInUsd',
            field=models.FloatField(default=1.5),
        ),
        migrations.AlterField(
            model_name='covid19',
            name='avgDailyIncomePopulation',
            field=models.FloatField(default=0.17),
        ),
    ]
