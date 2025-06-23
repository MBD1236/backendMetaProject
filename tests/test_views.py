from django.test import TestCase, Client
from restaurant.models import Menu
from restaurant.serializers import MenuItemSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=50, inventory=50)

    def test_getall(self):
        client = Client()
        response = client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuItemSerializer(menus, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)