# Generated by Django 4.2.3 on 2023-08-13 19:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(max_length=20, null=True),
        ),
    ]
