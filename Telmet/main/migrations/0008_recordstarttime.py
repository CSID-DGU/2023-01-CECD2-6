# Generated by Django 4.1.7 on 2023-05-06 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0007_delete_recordstarttime"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecordStartTime",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("time", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
