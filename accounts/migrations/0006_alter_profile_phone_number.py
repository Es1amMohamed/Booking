# Generated by Django 4.2.3 on 2023-08-16 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=1, max_length=20, unique=True),
        ),
    ]