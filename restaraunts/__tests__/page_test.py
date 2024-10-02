from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class RestaurantViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_restaurant_list_view(self):
        response = self.client.get(reverse('restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurants/restaurant_list.html')

    def test_restaurant_detail_view(self):
        #  тестовий ресторан
        restaurant = Restaurant.objects.create(name="Test Restaurant")
        response = self.client.get(reverse('restaurant_detail', args=[restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'restaurants/restaurant_detail.html')
