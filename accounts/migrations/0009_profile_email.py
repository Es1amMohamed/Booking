# Generated by Django 4.2.3 on 2023-08-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0008_alter_profile_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="email",
            field=models.EmailField(default=1, max_length=254, unique=True),
        ),
    ]
