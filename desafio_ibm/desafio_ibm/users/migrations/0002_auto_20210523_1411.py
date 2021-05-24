# Generated by Django 3.1.11 on 2021-05-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="street",
            field=models.CharField(blank=True, max_length=255, verbose_name="Rua"),
        ),
        migrations.AddField(
            model_name="user",
            name="street_number",
            field=models.CharField(blank=True, max_length=10, verbose_name="Rua"),
        ),
    ]
