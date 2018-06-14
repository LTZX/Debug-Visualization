    @staticmethod
    def lookup(email):
        """Get a User with the given email address, or None."""
        return User.query.filter_by(email=email).one_or_none()

