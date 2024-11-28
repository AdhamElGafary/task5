# tests/test_models.py
import unittest
from models import Product  # Assuming your Product model is in the models.py file
from faker import Faker

fake = Faker()

class TestProductModel(unittest.TestCase):

    def test_list_all_products(self):
        # Create and save multiple fake products
        products = []
        for _ in range(5):
            product = Product(name=fake.company(),
                              description=fake.text(max_nb_chars=200),
                              price=99.99,
                              sku=fake.uuid4(),
                              category=fake.word())
            product.save()  # Assuming the 'save' method persists the product
            products.append(product)
        
        # Simulate the "list all" operation (fetch all products)
        all_products = Product.list_all()  # Assuming 'list_all' fetches all products
        
        # Check that the list is not empty and contains the correct number of products
        self.assertGreater(len(all_products), 0)
        self.assertEqual(len(all_products), 5)  # Adjust based on how many you created

        # Check that each product in the list is a valid Product instance
        for product in all_products:
            self.assertIsInstance(product, Product)

if __name__ == '__main__':
    unittest.main()
