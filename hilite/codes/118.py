    def size(self):
        return GroupMember.query.filter_by(group=self).count()

