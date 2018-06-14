    def can(object, user, course, action):
        if user.is_admin:
            return True
        return False


