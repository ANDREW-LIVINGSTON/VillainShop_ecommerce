# Generated by Django 2.2.4 on 2021-08-10 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0009_auto_20210809_2241'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='cart_total',
            field=models.FloatField(default=0.0),
        ),
    ]
