# Generated by Django 3.0.4 on 2020-04-18 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airtrans', '0008_auto_20200418_2315'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='boarding_passes',
            unique_together={('ticket_no', 'flight_id')},
        ),
    ]
