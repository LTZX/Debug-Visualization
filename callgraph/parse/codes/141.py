    def test_testing_login(self):
        """GET /testing-login should show a test login page."""
        response = self.client.get('/testing-login')
        self.assert_200(response)
        self.assert_template_used('testing-login.html')

