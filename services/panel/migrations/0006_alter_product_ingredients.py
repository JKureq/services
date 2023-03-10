# Generated by Django 4.1.6 on 2023-02-14 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("panel", "0005_alter_product_duration_alter_product_ingredients_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="ingredients",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="products", to="panel.ingredient"
            ),
        ),
    ]
