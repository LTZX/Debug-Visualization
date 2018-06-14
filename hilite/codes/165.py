    def test_home(self):
        """Tests that the home page loads."""
        response = self.client.get('/')
        self.assert_200(response)
