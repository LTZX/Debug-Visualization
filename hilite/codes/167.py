    def test_lookup(self):
        email = 'martymcfly@aol.com'

        user = User.lookup(email)
        assert user is None

        db.session.add(User(email=email))
        db.session.commit()

        user = User.lookup(email)
