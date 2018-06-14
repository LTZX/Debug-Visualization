    def has_status(self, user, status):
        return GroupMember.query.filter_by(
            user=user,
            group=self,
            status=status
        ).count() > 0

