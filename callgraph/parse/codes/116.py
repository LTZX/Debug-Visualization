    @staticmethod
    def lookup(user, assignment):
        member = GroupMember.query.filter_by(
            user=user,
            assignment=assignment
        ).one_or_none()
        if member:
            return member.group

