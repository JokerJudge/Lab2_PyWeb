# Generated by Django 3.0.4 on 2020-04-18 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airtrans', '0004_auto_20200418_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircrafts',
            name='range',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='airports',
            name='coordinates',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='airports',
            name='timezone',
            field=models.CharField(blank=True, max_length=12),
        ),
        migrations.AlterField(
            model_name='flights',
            name='actual_arrival',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='flights',
            name='actual_departure',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='tickets',
            name='contact_data',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
