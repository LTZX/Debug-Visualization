    def test_login(self):
        """GET /login should redirect to Google OAuth."""
        response = self.client.get('/login')
        assert response.location.startswith('https://accounts.google.com/o/oauth2/auth')

