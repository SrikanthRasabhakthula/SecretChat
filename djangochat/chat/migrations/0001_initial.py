# Generated by Django 5.1 on 2024-10-18 12:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Messages",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.CharField(max_length=10000000)),
                (
                    "date",
                    models.DateTimeField(
                        blank=True,
                        default=datetime.datetime(2024, 10, 18, 17, 40, 27, 219496),
                    ),
                ),
                ("user", models.CharField(max_length=10000000)),
                ("room", models.CharField(max_length=10000000)),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=1000000)),
            ],
        ),
    ]
