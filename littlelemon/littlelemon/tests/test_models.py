from django.test import TestCase

from LittleLemonAPI.models import Category, MenuItem

# Create your tests here.
class MenuItemTest(TestCase):
  def test_get_item(self):
    category = Category.objects.create(title='Dessert')
    self.assertEqual(str(category), 'Dessert')
    item = MenuItem.objects.create(title="IceCream", slug='icecream', category=category, price=80, featured=False, inventory=100)
    self.assertEqual(str(item), '(Dessert) IceCream : $80.00 [False] (100)')
