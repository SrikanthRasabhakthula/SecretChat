# Generated by Django 5.1 on 2024-10-18 13:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chat", "0002_alter_messages_date_alter_messages_room_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="messages",
            name="room",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="chat.room"
            ),
        ),
    ]
