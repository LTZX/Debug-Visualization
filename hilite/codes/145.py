    def test_test_config(self):
        """ Tests if the test config loads correctly """

        app = create_app('server.settings.test.TestConfig')
        test_db = 'postgresql://postgres:@localhost:5432/oktest'

        assert app.config['DEBUG'] is True
        assert app.config['SQLALCHEMY_DATABASE_URI'] == test_db
