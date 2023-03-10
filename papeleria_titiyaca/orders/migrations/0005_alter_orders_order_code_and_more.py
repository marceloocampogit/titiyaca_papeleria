# Generated by Django 4.1.4 on 2023-01-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_orderstatus_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_code',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='payment_method_large',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
