# Generated by Django 4.1.4 on 2023-01-25 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_products_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='category_name',
            field=models.CharField(max_length=100),
        ),
    ]
