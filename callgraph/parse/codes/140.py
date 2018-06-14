    def test_restricted(self):
        """User should see /restricted if logged in, but not if logged out."""
        self.login(self.email)
        response = self.client.get('/restricted')
        self.assert_200(response)

        self.client.get('/logout')
        response = self.client.get('/restricted')
