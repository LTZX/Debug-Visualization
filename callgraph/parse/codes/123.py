    def has_role(self, course, role):
        if self.course != course:
            return False
        return self.role == role

