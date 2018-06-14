    def login(self, email):
        """ Log in as an email address """
        response = self.client.post('/testing-login/authorized', data={
            'email': email
        }, follow_redirects=True)
