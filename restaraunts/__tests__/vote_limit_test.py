from datetime import timedelta
from django.utils import timezone

class OneVotePerDayTests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.vote_url = reverse('vote')
        self.vote = Vote.objects.create(user=self.user, choice='Fish and Chips', voted_at=timezone.now())

    def test_vote_once_per_day(self):
        data = {'choice': 'Grilled Chicken Salad'}
        response = self.client.post(self.vote_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['detail'], 'You can only vote once per day')
