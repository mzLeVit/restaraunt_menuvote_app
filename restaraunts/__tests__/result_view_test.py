class ResultsViewTests(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        Vote.objects.create(user=self.user, choice='Fish and Chips')

    def test_view_results(self):
        response = self.client.get(reverse('results_page'))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, 'Fish and Chips')
        self.assertContains(response, 'Total Votes: 1')
