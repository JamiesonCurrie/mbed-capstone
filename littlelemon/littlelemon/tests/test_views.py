from django.test import TestCase
from django.urls import reverse

from LittleLemonAPI.models import Category, MenuItem

# Create your tests here.
class MenuViewTest(TestCase):
  def setUp(self):
    category = Category.objects.create(title='Dessert')
    MenuItem.objects.create(title="IceCream", slug='icecream', category=category, price=80, featured=False, inventory=100)
    MenuItem.objects.create(title="Apple Pie", slug='pie', category=category, price=7.99, featured=True, inventory=56)

  def test_getall(self):
    url              = reverse("littlelemon-api:menu-items")
    response         = self.client.get(url)
    response_content = response.content.decode("utf-8")
    self.assertJSONEqual(response_content, [
      {'id':1, 'title':"IceCream", 'slug':'icecream', 'category':1, 'price':'80.00', 'featured':False, 'inventory':100},
      {'id':2, 'title':"Apple Pie", 'slug':'pie', 'category':1, 'price':'7.99', 'featured':True, 'inventory':56}
    ])