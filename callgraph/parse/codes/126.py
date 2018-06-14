    def enrollments(self, roles=['student']):
        return [e for e in self.participations if e.role in roles]

