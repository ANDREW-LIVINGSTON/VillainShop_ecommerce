# Generated by Django 2.2.4 on 2021-04-02 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0005_auto_20210401_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='ordered_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='ecommerce_app.Product'),
        ),
    ]
