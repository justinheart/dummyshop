from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    stock_pcs = models.IntegerField(default=None, blank=True, null=True)
    price = models.IntegerField(default=None, blank=True, null=True)
    shop_id = models.CharField(max_length=2, default=None, blank=True, null=True)
    vip = models.BooleanField(default=None, blank=True, null=True)

class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    product = models.ForeignKey('Product', to_field='product_id', on_delete=models.CASCADE)
    qty = models.IntegerField(default=None, blank=True, null=True)
    price = models.IntegerField(default=None, blank=True, null=True)
    shop_id = models.CharField(default=None, blank=True, null=True, max_length=2)
    customer_id = models.IntegerField(default=None, blank=True, null=True)
