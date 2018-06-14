    def is_enrolled(self, user):
        return Participant.query.filter_by(
            user=user,
            course=self
        ).count() > 0


