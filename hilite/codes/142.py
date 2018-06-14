    def test_testing_login_fail(self):
        """GET /testing-login should 404 if TESTING_LOGIN config is not set."""
        app = self.create_app()
        app.config['TESTING_LOGIN'] = False
        response = app.test_client().get('/testing-login')
        self.assert_404(response)

