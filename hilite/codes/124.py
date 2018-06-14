    def is_staff(self, course):
        return self.course == course and self.role in STAFF_ROLES

