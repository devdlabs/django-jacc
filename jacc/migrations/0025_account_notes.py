# Generated by Django 3.2 on 2021-04-23 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jacc", "0024_accountentry_cached_balance"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="notes",
            field=models.TextField(blank=True, default="", verbose_name="notes"),
        ),
    ]