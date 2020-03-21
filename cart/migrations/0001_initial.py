# Generated by Django 3.0.4 on 2020-03-21 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('stock_pcs', models.IntegerField(blank=True, default=None, null=True)),
                ('price', models.IntegerField(blank=True, default=None, null=True)),
                ('shop_id', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('vip', models.BooleanField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.IntegerField(primary_key=True, serialize=False)),
                ('qty', models.IntegerField(blank=True, default=None, null=True)),
                ('price', models.IntegerField(blank=True, default=None, null=True)),
                ('shop_id', models.CharField(blank=True, default=None, max_length=2, null=True)),
                ('customer_id', models.IntegerField(blank=True, default=None, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Product')),
            ],
        ),
    ]