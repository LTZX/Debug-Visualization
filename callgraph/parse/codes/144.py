    def test_dev_config(self):
        """ Tests if the development config loads correctly """

        app = create_app('server.settings.dev.DevConfig')
        dev_db = 'postgresql://postgres:@localhost:5432/okdev'

        assert app.config['DEBUG'] is True
        assert app.config['SQLALCHEMY_DATABASE_URI'] == dev_db
        assert app.config['CACHE_TYPE'] == 'simple'

