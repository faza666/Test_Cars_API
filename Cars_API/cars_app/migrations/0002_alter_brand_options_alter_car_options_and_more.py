# Generated by Django 4.0.6 on 2022-08-07 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("cars_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="brand",
            options={"verbose_name": "Brand", "verbose_name_plural": "Brands"},
        ),
        migrations.AlterModelOptions(
            name="car",
            options={"verbose_name": "Car", "verbose_name_plural": "Cars"},
        ),
        migrations.AlterModelOptions(
            name="model",
            options={"verbose_name": "Model", "verbose_name_plural": "Models"},
        ),
    ]