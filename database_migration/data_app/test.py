from django.test import TestCase
from myapp.models import User, Address, Item

class TestSQLQueries(TestCase):
    def test_foreign_key_relationships(self):
        user = User.objects.create(name='Test User')
        address = Address.objects.create(email_address='test@example.com', user=user)
        item = Item.objects.create(name='Test Item', description='Test Description', user=user)

        self.assertEqual(address.user, user)
        self.assertEqual(item.user, user)

    def test_view_query(self):
        response = self.client.get('/combined-data/')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            [{"name": "John", "address__email_address": "john@example.com", "item__name": "Book", "item__description": "A good book"},
             {"name": "Alice", "address__email_address": "alice@example.com", "item__name": "Laptop", "item__description": "A powerful laptop"}]
        )
