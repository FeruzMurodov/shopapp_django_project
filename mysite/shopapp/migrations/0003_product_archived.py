# Generated by Django 5.1.3 on 2024-11-17 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_product_created_at_product_discount_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
