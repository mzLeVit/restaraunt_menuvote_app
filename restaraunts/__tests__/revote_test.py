class UpdateVoteTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')
        self.vote_url = reverse('vote')
        Vote.objects.create(user=self.user, choice='Fish and Chips')

    def test_vote_update(self):
        data = {'choice': 'Grilled Chicken Salad'}
        response = self.client.post(self.vote_url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(Vote.objects.filter(user=self.user, choice='Grilled Chicken Salad').exists())
