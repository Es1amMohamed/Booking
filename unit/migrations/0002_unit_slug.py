# Generated by Django 4.2.3 on 2023-07-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("unit", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="unit",
            name="slug",
            field=models.SlugField(blank=True, null=True),
        ),
    ]
