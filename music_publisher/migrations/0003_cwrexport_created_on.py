# Generated by Django 3.2.6 on 2021-08-16 15:15

from django.db import migrations, models
from django.utils.timezone import datetime, make_aware, get_fixed_timezone


class Migration(migrations.Migration):
    dependencies = [
        ("music_publisher", "0002_mayday"),
    ]

    operations = [
        migrations.AddField(
            model_name="cwrexport",
            name="created_on",
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
