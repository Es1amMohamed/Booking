# Generated by Django 4.2.3 on 2023-08-02 19:19

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("unit", "0004_alter_unitbook_adults_alter_unitbook_children"),
    ]

    operations = [
        migrations.AlterField(
            model_name="unitbook",
            name="adults",
            field=models.IntegerField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1
            ),
        ),
        migrations.AlterField(
            model_name="unitbook",
            name="children",
            field=models.IntegerField(
                choices=[(1, 1), (2, 2), (3, 3), (4, 4)], default=1
            ),
        ),
    ]
