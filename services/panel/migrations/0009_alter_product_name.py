# Generated by Django 4.1.6 on 2023-02-15 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panel", "0008_alter_ingredient_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]