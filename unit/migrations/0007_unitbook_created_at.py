# Generated by Django 4.2.3 on 2023-08-16 17:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("unit", "0006_alter_unitbook_adults_alter_unitbook_children"),
    ]

    operations = [
        migrations.AddField(
            model_name="unitbook",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
