from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Vote

class VoteTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.vote_url = reverse('vote')

    def test_vote_submission(self):
        data = {'choice': 'Fish and Chips'}
        response = self.client.post(self.vote_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Vote.objects.filter(user=self.user, choice='Fish and Chips').exists())
