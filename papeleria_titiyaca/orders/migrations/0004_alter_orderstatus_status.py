# Generated by Django 4.1.4 on 2023-01-21 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_orderitems_item_code_alter_orders_order_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderstatus',
            name='status',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
