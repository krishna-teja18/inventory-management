from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Item

class ItemTests(APITestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Obtain a JWT token
        self.login_url = reverse('token_obtain_pair')
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword'})
        self.token = response.data['access']

        # Set the authentication headers
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

        # Set up item data and URLs
        self.create_url = reverse('create_item')
        self.item_data = {'name': 'Test Item', 'description': 'Test Description'}

    def test_create_item(self):
        # Test creating an item
        response = self.client.post(self.create_url, self.item_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        # Test retrieving an item
        item = Item.objects.create(**self.item_data)
        response = self.client.get(reverse('get_item', args=[item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        # Test updating an item
        item = Item.objects.create(**self.item_data)
        updated_data = {'name': 'Updated Item', 'description': 'Updated Description'}
        response = self.client.put(reverse('update_item', args=[item.id]), updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_item(self):
        # Test deleting an item
        item = Item.objects.create(**self.item_data)
        response = self.client.delete(reverse('delete_item', args=[item.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
