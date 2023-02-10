from main import Cart, Items
import unittest

class CartTest(unittest.TestCase):
    def test_add_items(self):
        test_cart = Cart()
        test_cart.add_items('eggs', '20')

        self.assertEqual(test_cart.carts[0].item, 'eggs')
        self.assertEqual(test_cart.carts[0].quantity, 20)
        self.assertEqual(len(test_cart.carts), 1)

    def test_remove_items(self):
        test_cart = Cart()
        test_cart.add_items('eggs', '20')
        test_cart.remove_items('eggs', '10')

        self.assertEqual(test_cart.carts[0].item, 'eggs')
        self.assertEqual(test_cart.carts[0].quantity, 10)

        test_cart.remove_items('eggs', '10')

        self.assertEqual(len(test_cart.carts), 0)

    def test_show_list(self):
        test_cart = Cart()
        test_cart.add_items('eggs', '20')
        test_cart.add_items('milk', '5')

        test_cart.show_list()
        result = (f'Currently you have {str(test_cart.carts[0].quantity)} {str(test_cart.carts[0].item)} in your cart.')
        expected_result = 'Currently you have 20 eggs in your cart.'
        self.assertEqual(result, expected_result)

unittest.main()