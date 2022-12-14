# Generated by Django 4.1 on 2022-08-10 06:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_alter_sale_amount_received_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='amount_received',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='date_of_purchase',
            field=models.CharField(blank=True, default=datetime.datetime(2022, 8, 10, 14, 23, 54), max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='sale',
            name='issued_to',
            field=models.CharField(default='Someone', max_length=50),
        ),
        migrations.AlterField(
            model_name='sale',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
