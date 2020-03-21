from django.test import TestCase
from cart.models import Product, Order

# Create your tests here.
class ProductModelTest(TestCase):

    def test_saving_and_retrieving_products(self):
        first_product = Product()
        first_product.product_id = 1
        first_product.stock_pcs = 6
        first_product.price = 150
        first_product.shop_id = 'um'
        first_product.vip = False
        first_product.save()

        second_product = Product()
        second_product.product_id = 2
        second_product.stock_pcs = 10
        second_product.price = 800
        second_product.shop_id = 'ps'
        second_product.vip = True
        second_product.save()

        saved_products = Product.objects.all()
        self.assertEqual(saved_products.count(), 2)

        first_saved_product = saved_products[0]
        self.assertEqual(first_saved_product.product_id, 1)
        self.assertEqual(first_saved_product.stock_pcs, 6)
        self.assertEqual(first_saved_product.price, 150)
        self.assertEqual(first_saved_product.shop_id, 'um')
        self.assertEqual(first_saved_product.vip, False)

        second_saved_product = saved_products[1]
        self.assertEqual(second_saved_product.product_id, 2)
        self.assertEqual(second_saved_product.stock_pcs, 10)
        self.assertEqual(second_saved_product.price, 800)
        self.assertEqual(second_saved_product.shop_id, 'ps')
        self.assertEqual(second_saved_product.vip, True)

    def test_saving_and_retrieving_orders(self):
        first_product = Product()
        first_product.product_id = 1
        first_product.stock_pcs = 6
        first_product.price = 150
        first_product.shop_id = 'um'
        first_product.vip = False
        first_product.save()

        second_product = Product()
        second_product.product_id = 2
        second_product.stock_pcs = 10
        second_product.price = 800
        second_product.shop_id = 'ps'
        second_product.vip = True
        second_product.save()

        saved_products = Product.objects.all()

        first_order = Order(product=saved_products[0])
        first_order.order_id = 1
        first_order.product_id = 1
        first_order.qty = 6
        first_order.price = saved_products[0].price
        first_order.shop_id = saved_products[0].shop_id
        first_order.customer_id = 1
        first_order.save()

        second_order = Order(product=saved_products[1])
        second_order.order_id = 2
        second_order.product_id = saved_products[1].product_id
        second_order.qty = 3
        second_order.price = saved_products[1].price
        second_order.shop_id = saved_products[1].shop_id
        second_order.customer_id = 2
        second_order.save()

        saved_orders = Order.objects.all()
        self.assertEqual(saved_orders.count(), 2)

        first_saved_order = saved_orders[0]
        self.assertEqual(first_saved_order.order_id, 1)
        self.assertEqual(first_saved_order.product_id, 1)
        self.assertEqual(first_saved_order.qty, 6)
        self.assertEqual(first_saved_order.price, 150)
        self.assertEqual(first_saved_order.shop_id, 'um')
        self.assertEqual(first_saved_order.customer_id, 1)

        second_saved_order = saved_orders[1]
        self.assertEqual(second_saved_order.order_id, 2)
        self.assertEqual(second_saved_order.product_id, 2)
        self.assertEqual(second_saved_order.qty, 3)
        self.assertEqual(second_saved_order.price,800)
        self.assertEqual(second_saved_order.shop_id, 'ps')
        self.assertEqual(second_saved_order.customer_id, 2)
