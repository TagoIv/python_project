import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_product_creation(self):
        response = self.app.post('/api/products', json={"name": "Test Product", "price": 10.99})
        self.assertEqual(response.status_code, 201)
        self.assertIn(b'"message": "Product added successfully."', response.data)

    # Add more test methods as needed

if __name__ == '__main__':
    unittest.main()
