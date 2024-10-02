class NoVotesTests(APITestCase):
    
    def test_no_votes_message(self):
        response = self.client.get(reverse('results_page'))

        self.assertContains(response, 'No votes have been cast yet')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
