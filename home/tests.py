from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Category, Products
from django.utils.dateparse import parse_date
from django.utils.timezone import make_aware
from datetime import datetime
import warnings

class APITestCase(TestCase):
    def setUp(self):
        warnings.filterwarnings(
            "ignore",
            message="DateTimeField .* received a naive datetime",
            category=RuntimeWarning,
            module='django.db.models.fields',
        )
        # Set up user and client for authentication
        self.user = User.objects.create_user(username='krushang', password='krushangsatani')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        # Pre-create a category for tests that require it
        self.category_name = "Electronics"
        Category.objects.create(name=self.category_name)

    def test_get_products(self):
        url = reverse('api:get_products')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('categories', response.data)
        self.assertIn('products', response.data)

    def test_create_category(self):
        url = reverse('api:save_category')
        data = {'name': 'Unique Test Category'}
        initial_count = Category.objects.count()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), initial_count + 1)
        self.assertEqual(Category.objects.filter(name='Unique Test Category').count(), 1)

    def test_create_product(self):
        url = reverse('api:save_product')
        data = {
            'name': 'New Smartphone',
            'sku': '12345',
            'category': self.category_name,
            'stock_status': 1,  # Assuming 1 represents 'in_stock'
            'available_stock': 100,
            'tags': ['smartphone', 'electronics', 'mobile']
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Products.objects.count(), 1)
        product = Products.objects.first()
        self.assertEqual(product.name, 'New Smartphone')
        self.assertEqual(product.category.name, self.category_name)

    # Uncomment and adapt the rest of the tests as needed
    # Ensure you adjust any setup or assumptions according to your model and view logic

    def test_get_auth_token(self):
        url = reverse('api:api_token_auth')
        data = {"username": "krushang", "password": "krushangsatani"}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['token'], self.token.key)

    def test_register_user(self):
        url = reverse('api:register_user')
        data = {"username": "newuser", "password": "newpassword123", "email": "newuser@example.com"}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_change_password(self):
        # Ensure the user is authenticated for this operation if required
        self.client.force_authenticate(user=self.user)
        
        url = reverse('api:change_password')
        data = {"username": "krushang", "newpassword": "new_password123"}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()  # Refresh the user instance to get the updated password
        self.assertTrue(self.user.check_password("new_password123"))

    
    def create_product_with_date(self, created_at_date_str):
        created_at_datetime = datetime.strptime(created_at_date_str, "%Y-%m-%d")
        created_at_datetime = make_aware(created_at_datetime)  # Ensure datetime is timezone-aware
        category = Category.objects.get(name=self.category_name)  # Retrieve the category

        # Create and save the product
        product = Products.objects.create(
            name=f"Product {created_at_date_str}",
            sku=f"SKU-{created_at_date_str}",
            category=category,
            stock_status=1,  # Assuming this is a valid stock status
            available_stock=100,
            created_at=created_at_datetime  # Ensure this field exists in your Products model
        )
        return product

    def test_get_products_with_date_filter(self):
        # Assuming you have a method to create products with specific dates
        self.create_product_with_date("2023-01-01")
        self.create_product_with_date("2023-01-15")
        
        url = reverse('api:get_products')
        start_date = '2023-01-01'
        end_date = '2023-01-31'
        response = self.client.get(f"{url}?start_date={start_date}&end_date={end_date}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert based on expected response structure
        # self.assertTrue(len(response.data['products']) >= 2)  # Adjust based on actual data and response format
    
    